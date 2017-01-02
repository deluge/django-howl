from datetime import timedelta

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils import timezone
from django.utils.functional import curry
from django.utils.module_loading import import_string
from django.utils.translation import ugettext_lazy as _

from .conf.settings import HOWL_OPERATORS
from .operators import BaseOperator
from .signals import alert_clear, alert_notify, alert_wait


def do_operator_setup(cls, **kwargs):
    operators = {}

    for operator_path in getattr(settings, 'HOWL_OPERATORS', HOWL_OPERATORS):
        operator_class = import_string(operator_path)

        if not issubclass(operator_class, BaseOperator):
            raise TypeError(
                'Operator "{0}" must be of type: "howl.operators.BaseOperator"'.format(
                    operator_class))

        operator_name = operator_class.__name__

        if operator_name in operators:
            raise ImproperlyConfigured(
                'Operator named "{0}" already exists.'.format(operator_name))

        operators[operator_name] = operator_class

    choices = [
        (name, operator_class.display_name) for name, operator_class in operators.items()
    ]

    cls.operators = operators
    cls.operator_choices = choices

    operator = cls._meta.get_field('operator')
    operator.choices.extend(cls.operator_choices)
    operator.choices.sort(key=lambda item: item[0])

    cls.get_operator_display = curry(cls._get_FIELD_display, field=operator)


class Observer(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    operator = models.CharField(_('Operator type'), max_length=32, choices=[])
    value = models.FloatField(_('Value'))
    waiting_period = models.PositiveIntegerField(
        _('Waiting period'), help_text=_('In seconds'))
    alert_every_time = models.BooleanField(_('Alert every time'), default=False)

    class Meta:
        verbose_name = _('Observer')
        verbose_name_plural = _('Observers')
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_alert_identifier(self, **kwargs):
        if kwargs.get('identifier', None):
            return kwargs['identifier']

        return 'howl-observer:{0}'.format(self.pk)

    def get_alert(self, compare_value, **kwargs):
        operator_class = self.operators[self.operator]

        if operator_class(self).compare(compare_value):
            Alert.clear(compare_value, observer=self, **kwargs)
            return None

        return Alert.set(compare_value, observer=self, **kwargs)

    def compare(self, compare_value, **kwargs):
        return self.get_alert(compare_value, **kwargs) is None


class Alert(models.Model):
    STATE_WAITING, STATE_NOTIFIED = range(0, 2)
    STATE_CHOICES = (
        (STATE_WAITING, _('Waiting')),
        (STATE_NOTIFIED, _('Notified')),
    )
    identifier = models.CharField(_('Identifier'), max_length=64, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.CharField(_('Value'), max_length=255, blank=True, null=True)
    state = models.PositiveSmallIntegerField(
        _('State'), choices=STATE_CHOICES, default=STATE_WAITING)

    class Meta:
        verbose_name = _('Alert')
        verbose_name_plural = _('Alerts')
        ordering = ('-timestamp',)

    def __str__(self):
        return _('Alert for {0}').format(self.identifier)

    @classmethod
    def set(cls, value=None, **kwargs):
        if 'observer' in kwargs:
            identifier = kwargs['observer'].get_alert_identifier(**kwargs)
            waiting_period = kwargs['observer'].waiting_period
            alert_every_time = kwargs['observer'].alert_every_time
        else:
            if 'identifier' not in kwargs:
                raise ValueError('`observer` or `identifier` required.')
            identifier = kwargs['identifier']
            waiting_period = kwargs.get('waiting_period', 0)
            alert_every_time = kwargs.get('alert_every_time', False)

        obj, created = Alert.objects.get_or_create(
            identifier=identifier, defaults={'value': value})

        if created and waiting_period > 0:
            alert_wait.send(sender=cls, instance=obj, value=value, **kwargs)
            return obj

        alert_time = obj.timestamp + timedelta(seconds=waiting_period)

        if alert_time < timezone.now():
            if obj.state == obj.STATE_NOTIFIED and alert_every_time:
                obj.value = value
                obj.save(update_fields=['value'])
                alert_notify.send(sender=cls, instance=obj, value=value, **kwargs)

            if obj.state == obj.STATE_WAITING:
                obj.value = value
                obj.state = obj.STATE_NOTIFIED
                obj.save(update_fields=['value', 'state'])
                alert_notify.send(sender=cls, instance=obj, value=value, **kwargs)

        return obj

    @classmethod
    def clear(cls, value=None, **kwargs):
        if 'observer' in kwargs:
            identifier = kwargs['observer'].get_alert_identifier(**kwargs)
        else:
            if 'identifier' not in kwargs:
                raise ValueError('`observer` or `identifier` required.')
            identifier = kwargs['identifier']

        try:
            obj = Alert.objects.get(identifier=identifier)
            alert_clear.send(sender=cls, instance=obj, value=value, **kwargs)
            obj.delete()
        except Alert.DoesNotExist:
            pass
