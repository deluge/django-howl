from django.apps import AppConfig


class PushoverConfig(AppConfig):
    name = "pushover"

    def ready(self):
        import pushover.handlers  # noqa
