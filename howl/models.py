from datetime import datetime, timedelta

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .operators import get_operator_class, get_operator_types
from .signals import alert_clear, alert_notify, alert_wait


class Observer(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    operator = models.CharField(
        _('Operator type'), max_length=32, choices=get_operator_types())
    value = models.PositiveIntegerField(_('Value'))
    waiting_period = models.PositiveIntegerField(_('Waiting period'), help_text=_('In seconds'))
    alert_every_time = models.BooleanField(_('Alert every time'), default=False)

    class Meta:
        verbose_name = _('Observer')
        verbose_name_plural = _('Observers')
        ordering = ('name',)

    def __str__(self):
        return self.name

    def compare(self, compare_value):
        operator_class = get_operator_class(self.operator)

        if operator_class(self).compare(compare_value):
            Alert.clear(self)
            return False

        Alert.set(self, compare_value)
        return True


class Alert(models.Model):
    STATE_WAITING, STATE_NOTIFIED = range(0, 2)
    STATE_CHOICES = (
        (STATE_WAITING, _('Waiting')),
        (STATE_NOTIFIED, _('Notified')),
    )

    observer = models.ForeignKey(Observer, verbose_name=_('Observer'))
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.CharField(_('Value'), max_length=255)
    state = models.PositiveSmallIntegerField(
        _('State'), choices=STATE_CHOICES, default=STATE_WAITING)

    class Meta:
        verbose_name = _('Alert')
        verbose_name_plural = _('Alerts')
        ordering = ('-timestamp',)

    def __str__(self):
        return _('Alert (ID: {0}) for {1}').format(self.pk, self.observer.name)

    @classmethod
    def set(cls, observer, compare_value):
        obj, created = Alert.objects.get_or_create(
            observer=observer, defaults={'value': compare_value})

        if created:
            alert_wait.send(sender=cls, instance=obj)
            return True

        alert_time = obj.timestamp + timedelta(seconds=observer.waiting_period)

        if alert_time < datetime.now():
            if obj.state == obj.STATE_NOTIFIED and observer.alert_every_time:
                obj.value = compare_value
                obj.save(update_fields=['value'])
                alert_notify.send(sender=cls, instance=obj)

            if obj.state == obj.STATE_WAITING:
                obj.value = compare_value
                obj.state = obj.STATE_NOTIFIED
                obj.save(update_fields=['value', 'state'])
                alert_notify.send(sender=cls, instance=obj)

    @classmethod
    def clear(cls, observer):
        try:
            obj = Alert.objects.get(observer=observer)
            alert_clear.send(sender=cls, instance=obj)
            obj.delete()
        except Alert.DoesNotExist:
            pass
