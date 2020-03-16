import warnings


warnings.warn((
    'django-howl is not maintained anymore. Please use '
    'django-pushover. (https://pypi.org/project/django-pushover/)'
), DeprecationWarning)


__version__ = '1.0.5'
default_app_config = 'howl.apps.DjangoHowlConfig'
