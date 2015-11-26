from django.utils.translation import ugettext_lazy as _


def add_operator_type(operator_class):
    # Fail silently if we try to double register operator classes.
    if operator_class.__name__ in add_operator_type._REGISTRY:
        return False

    add_operator_type._REGISTRY[operator_class.__name__] = operator_class
    return True

add_operator_type._REGISTRY = {}


def get_operator_types():
    return sorted([
        (operator_class.__name__, operator_class.display_name)
        for operator_class in add_operator_type._REGISTRY.values()
    ])


class OperatorException(Exception):
    pass


class BaseOperator(object):
    display_name = None

    @classmethod
    def register(cls):
        return add_operator_type(cls)

    def __init__(self, observer):
        self.observer = observer

    def compare(self, compare_value):
        raise NotImplementedError('Method compare is not implemented.')


class EqualOperator(BaseOperator):
    display_name = _('Equals to value')

    def compare(self, compare_value):
        if self.observer.tolerance == 0:
            return self.observer.value == compare_value

        factor = self.observer.value * self.observer.tolerance / 100.0
        min_tolerance = float(self.observer.value - factor)
        max_tolerance = float(self.observer.value + factor)

        return min_tolerance <= float(compare_value) and max_tolerance >= float(compare_value)

EqualOperator.register()


class LowerThanOperator(BaseOperator):
    display_name = _('Lower than value')

    def compare(self, compare_value):
        if self.observer.tolerance == 0:
            return self.observer.value < compare_value

        factor = self.observer.value * self.observer.tolerance / 100.0
        max_tolerance = float(self.observer.value + factor)

        return float(compare_value) < max_tolerance

LowerThanOperator.register()


class GreaterThanOperator(BaseOperator):
    display_name = _('Greater than value')

    def compare(self, compare_value):
        if self.observer.tolerance == 0:
            return self.observer.value < compare_value

        factor = self.observer.value * self.observer.tolerance / 100.0
        min_tolerance = float(self.observer.value - factor)

        return float(compare_value) > min_tolerance

GreaterThanOperator.register()
