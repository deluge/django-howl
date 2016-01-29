from django.dispatch import Signal


alert_clear = Signal(providing_args=['instance', 'compare_value'])
alert_notify = Signal(providing_args=['instance', 'compare_value'])
alert_wait = Signal(providing_args=['instance', 'compare_value'])
