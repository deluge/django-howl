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


def get_operator_class(class_name):
    cls = add_operator_type._REGISTRY.get(class_name, None)

    if not cls:
        raise KeyError('Key "{0}" not in operator registry'.format(class_name))

    return cls


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
        return self.observer.value == compare_value

EqualOperator.register()


class LowerThanOperator(BaseOperator):
    display_name = _('Lower than value')

    def compare(self, compare_value):
        return compare_value < self.observer.value

LowerThanOperator.register()


class GreaterThanOperator(BaseOperator):
    display_name = _('Greater than value')

    def compare(self, compare_value):
        return compare_value > self.observer.value

GreaterThanOperator.register()
