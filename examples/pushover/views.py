from django.views.generic import TemplateVIew

from pushover.models import Watchdog


class SimpleView(TemplateVIew):
    template_name = 'pushover/index.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)

        watchdog_list = []

        for watchdog in Watchdog.objects.all():
            is_alert = watchdog.observer.compare(
                watchdog.number, watchdog=watchdog,
                identifier='watchdog:{0}'.format(watchdog.pk)
            )
            status = 'ALERT' if is_alert else 'OK'
            watchdog_list.append('Watchdog ID:{0} - {1}'.format(watchdog.pk, status))

        kwargs.update({
            'watchdog_list': watchdog_list,
        })

        return kwargs
