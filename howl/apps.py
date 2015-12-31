from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from .settings import SIGNALS


class DjangoHowlConfig(AppConfig):
    name = 'howl'
    verbose_name = _('Howl')

    def ready(self):
        if SIGNALS:  # pragma: nocover
            __import__(SIGNALS)
