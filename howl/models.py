from django.db import models
from django.utils.translation import ugettext_lazy as _


class Sensor(models.Model):
    VALUE_EQUALS, VALUE_LOWER, VALUE_GREATER = range(0, 3)

    VALUE_CHOICES = (
        (VALUE_EQUALS, _('Value euqals')),
        (VALUE_LOWER, _('Value lower than')),
        (VALUE_GREATER, _('Value greater than')),
    )

    name = models.CharField(_('Name'), max_length=255)
    value_type = models.PositiveIntegerField(
        _('Value type'), choices=VALUE_CHOICES, default=VALUE_GREATER)
    info = models.CharField(
        _('Info'), max_length=255, blank=True, null=True,
        help_text=_('Value for information notification')
    )
    warn = models.CharField(
        _('Warn'), max_length=255, blank=True, null=True,
        help_text=_('Value for warning notification')
    )
    critical = models.CharField(
        _('Critical'), max_length=255, blank=True, null=True,
        help_text=_('Value for critical notification')
    )
