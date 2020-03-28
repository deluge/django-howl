from django.conf import settings
from django.dispatch import receiver

from howl.models import Alert
from howl.signals import alert_clear, alert_notify, alert_wait

from .api import PushoverApi


def notify(level, instance, signal=None, **kwargs):
    title = kwargs.pop("title", instance)
    if "observer" in kwargs:
        title = "{0}: {1}".format(level.upper(), kwargs["observer"].name)

    api = PushoverApi(settings.PUSHOVER_TOKEN)
    api.send_notification(
        settings.PUSHOVER_RECIPIENT, title, level, alert=instance, **kwargs
    )


@receiver(alert_wait, sender=Alert)
def send_warning(sender, instance, **kwargs):
    notify("warning", instance, **kwargs)


@receiver(alert_notify, sender=Alert)
def send_alert(sender, instance, **kwargs):
    notify("critical", instance, **kwargs)


@receiver(alert_clear, sender=Alert)
def send_clear(sender, instance, **kwargs):
    notify("ok", instance, **kwargs)
