from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DjangoHowlConfig(AppConfig):
    name = 'howl'
    verbose_name = _('Howl')
