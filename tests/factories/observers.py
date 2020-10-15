from factory import Sequence
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from howl.models import Alert, Observer


class ObserverFactory(DjangoModelFactory):
    name = Sequence(lambda i: "observer {0}".format(i))
    operator = "EqualOperator"
    value = 50.1
    waiting_period = 0

    class Meta:
        model = Observer


class AlertFactory(DjangoModelFactory):
    identifier = Sequence(lambda i: "alert-{0}")
    value = FuzzyChoice(range(1, 10))

    class Meta:
        model = Alert
