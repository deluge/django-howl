from django.db import models
from django.utils.translation import ugettext_lazy as _

from .operators import get_operator_types


class Observer(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    operator = models.CharField(
        _('Operator type'), max_length=32, choices=get_operator_types())
    value = models.PositiveIntegerField(_('Value'))
    waiting_period = models.PositiveIntegerField(_('Waiting period'), help_text=_('In seconds'))

    class Meta:
        verbose_name = _('Observer')
        verbose_name_plural = _('Observers')
        ordering = ('name',)

    def __str__(self):
        return self.name

    def compare(self, compare_value):
        operator_class = self.operator
        return operator_class(self).compare(compare_value)


class Alert(models.Model):
    STATE_WAITING, STATE_NOTIFIED = range(0, 2)
    STATE_CHOICES = (
        (STATE_WAITING, _('Waiting')),
        (STATE_NOTIFIED, _('Notified')),
    )

    observer = models.ForeignKey(Observer, verbose_name=_('Observer'))
    timestamp = models.DateTimeField(auto_now_add=True)
    state = models.PositiveSmallIntegerField(_('State'), default=STATE_WAITING)

    class Meta:
        verbose_name = _('Alert')
        verbose_name_plural = _('Alerts')
        ordering = ('-timestamp',)

    def __str__(self):
        return _('Alert (ID: {0}) for {1}').format(self.pk, self.observer.name)
