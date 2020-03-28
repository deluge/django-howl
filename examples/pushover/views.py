from django.views.generic import TemplateView
from pushover.models import Watchdog


class AlertView(TemplateView):
    template_name = "pushover/index.html"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)

        watchdog_list = []

        for watchdog in Watchdog.objects.all():
            is_valid = watchdog.observer.compare(
                watchdog.number,
                watchdog=watchdog,
                identifier="watchdog:{0}".format(watchdog.pk),
            )

            watchdog_list.append(
                "Watchdog ID{0}: {1} with value {2} - {3}".format(
                    watchdog.pk,
                    watchdog.observer.name,
                    watchdog.number,
                    "OK" if is_valid else "ALERT",
                )
            )

        kwargs.update(
            {"watchdog_list": watchdog_list,}
        )

        return kwargs
