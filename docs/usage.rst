Usage
=====


Operator
--------

``django-howl`` comes with 3 standard operators by default:

* EqualOperator
* LowerThanOperator
* GreaterThanOperator

All operators are subclassed from ``howl.operators.BaseOperator``. If you wish to add your own one, you have to subclass from the ``BaseOperator`` and add a compare method.

One example could be:

.. code-block:: python

    from howl.operators import BaseOperator


    class MyOperator(BaseOperator):
        display_name = 'My new Operator'

        def compare(self, compare_value):
            if compare_value < 1:
                return False

            return self.observer.value % compare_value == 0

Now you have to add the new operator to ``settings.py``. If you want to use only your own one, then add:

``HOWL_OPERATORS = ('path.to.operator.MyOperator',)``

or if you want to use all including your one, then add:

.. code-block:: python

    HOWL_OPERATORS = (
        'howl.operators.EqualOperator',
        'howl.operators.LowerThanOperator',
        'howl.operators.GreaterThanOperator',
        'path.to.operator.MyOperator',
    )


Connect to signals
------------------

Next step is, that you have to connect with the signals. There are 3 types of signals:

* alert_wait (first time the comparison failed)
* alert_notify (comparison still fails after a specific time)
* alert_clear (after failure, the comparison is working again)

Create a file named ``handlers.py``. This should look like the following one:

.. code-block:: python

    from django.dispatch import receiver
    from howl.models import Alert
    from howl.signals import alert_clear, alert_notify, alert_wait


    @receiver(alert_wait, sender=Alert)
    def send_warning(sender, instance, **kwargs):
        # send info/warning notification


    @receiver(alert_notify, sender=Alert)
    def send_alert(sender, instance, **kwargs):
        # send critical notification


    @receiver(alert_clear, sender=Alert)
    def send_clear(sender, instance, **kwargs):
        # send all is working now notification

Last but not least you have to connect the handlers with the signals at the begining of the runtime of the wsgi process. In your ``apps.py`` add the following:

.. code-block:: python

    from django.apps import AppConfig


    class MyAppConfig(AppConfig):
        name = 'myapp'

        def ready(self):
            import myapp.handlers  # noqa

``import myapp.handlers`` this is the path where you put your ``handlers.py``

Next steps to be continued...
=============================

Now you can login to the admin and configure some observers and build some nice apps
with it.
