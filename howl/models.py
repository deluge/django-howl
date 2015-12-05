from datetime import datetime, timedelta

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .operators import get_operator_class, get_operator_types
from .signals import howl_alert_critical, howl_alert_delete, howl_alert_warn


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

    def alert(self, compare_value):
        operator_class = get_operator_class(self.operator)

        if operator_class(self).compare(compare_value):
            if Alert.objects.filter(observer=self).exists():
                alert = Alert.objects.get(observer=self)
                howl_alert_delete.send(sender=self.__class__, instance=alert)
                alert.delete()

            return False

        obj, created = Alert.objects.get_or_create(observer=self, defaults={'observer': self})

        if created:
            howl_alert_warn.send(sender=self.__class__, instance=obj)
        else:
            alert_time = obj.timestamp + timedelta(seconds=self.waiting_period)
            if alert_time < datetime.now():
                if not obj.state == obj.STATE_NOTIFIED:
                    obj.state = obj.STATE_NOTIFIED
                    obj.save()

                if self.alert_every_time:
                    howl_alert_critical.send(sender=self.__class__, instance=obj)

        return True


class Alert(models.Model):
    STATE_WAITING, STATE_NOTIFIED = range(0, 2)
    STATE_CHOICES = (
        (STATE_WAITING, _('Waiting')),
        (STATE_NOTIFIED, _('Notified')),
    )

    observer = models.ForeignKey(Observer, verbose_name=_('Observer'))
    timestamp = models.DateTimeField(auto_now_add=True)
    state = models.PositiveSmallIntegerField(
        _('State'), choices=STATE_CHOICES, default=STATE_WAITING)

    class Meta:
        verbose_name = _('Alert')
        verbose_name_plural = _('Alerts')
        ordering = ('-timestamp',)

    def __str__(self):
        return _('Alert (ID: {0}) for {1}').format(self.pk, self.observer.name)
