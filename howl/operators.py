from django.utils.translation import ugettext_lazy as _


class OperatorException(Exception):
    pass


class BaseOperator(object):
    display_name = None

    def __init__(self, observer):
        self.observer = observer

    def compare(self, compare_value):
        raise NotImplementedError('Method compare is not implemented.')


class EqualOperator(BaseOperator):
    display_name = _('Equals')

    def compare(self, compare_value):
        return self.observer.value == compare_value


class LowerThanOperator(BaseOperator):
    display_name = _('Lower than')

    def compare(self, compare_value):
        return compare_value < self.observer.value


class GreaterThanOperator(BaseOperator):
    display_name = _('Greater than')

    def compare(self, compare_value):
        return compare_value > self.observer.value
