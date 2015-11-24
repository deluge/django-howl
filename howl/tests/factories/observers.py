import factory

from howl import comparators
from howl.models import Alert, Observer


class ObserverFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda i: 'observer {0}'.format(i))
    comparator = comparators.EqualComparator.name
    value = 50
    waiting_period = 0

    class Meta:
        model = Observer


class AlertFactory(factory.DjangoModelFactory):
    observer = factory.SubFactory(ObserverFactory)

    class Meta:
        model = Alert
