from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DjangoHowlConfig(AppConfig):
    name = 'howl'
    verbose_name = _('Howl')

    def ready(self):
        from howl.models import do_howl_operator_setup

        model = self.get_model('Observer')
        do_howl_operator_setup(model)
