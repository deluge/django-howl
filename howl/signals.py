from django.dispatch import Signal


alert_clear = Signal(providing_args=['instance'])
alert_notify = Signal(providing_args=['instance'])
alert_wait = Signal(providing_args=['instance'])
