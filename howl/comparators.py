from django.utils.translation import ugettext_lazy as _


class BaseComparator(object):
    name = None
    display_name = None

    def __init__(self, observer):
        self.observer = observer

    def value_is_exceeded(self, compare_value):
        raise NotImplementedError('Method value_is_exceeded is not implemented.')


class EqualComparator(BaseComparator):
    name = 'equal'
    display_name = _('Equals to value')

    def value_is_exceeded(self, compare_value):
        if self.observer.tolerance == 0:
            return self.observer.value == compare_value

        factor = self.observer.value * self.observer.tolerance / 100.0
        min_tolerance = float(self.observer.value - factor)
        max_tolerance = float(self.observer.value + factor)

        return min_tolerance <= float(compare_value) and max_tolerance >= float(compare_value)


class LowerThanComparator(BaseComparator):
    name = 'lower'
    display_name = _('Lower than value')

    def value_is_exceeded(self, compare_value):
        if self.observer.tolerance == 0:
            return self.observer.value < compare_value

        factor = self.observer.value * self.observer.tolerance / 100.0
        max_tolerance = float(self.observer.value + factor)

        return float(compare_value) < max_tolerance


class GreaterThanComparator(BaseComparator):
    name = 'greater'
    display_name = _('Greater than value')

    def value_is_exceeded(self, compare_value):
        if self.observer.tolerance == 0:
            return self.observer.value < compare_value

        factor = self.observer.value * self.observer.tolerance / 100.0
        min_tolerance = float(self.observer.value - factor)

        return float(compare_value) > min_tolerance


COMPARATOR_CLASSES = (EqualComparator,)
COMPARATOR_CHOICES = [(cls.name, cls.display_name) for cls in COMPARATOR_CLASSES]
COMPARATOR_MAPPING = dict([(cls.name, cls) for cls in COMPARATOR_CLASSES])
