from django.dispatch import Signal


howl_alert_warn = Signal(providing_args=['instance'])
howl_alert_critical = Signal(providing_args=['instance'])
howl_alert_delete = Signal(providing_args=['instance'])
