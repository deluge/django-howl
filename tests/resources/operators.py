from howl.operators import BaseOperator


class NotSubclassOperator(object):
    pass


class TestOperator(BaseOperator):
    display_name = 'Test Operator'

    def compare(self, compare_value):
        return compare_value > self.testmodel.value
