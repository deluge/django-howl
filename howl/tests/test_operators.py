import pytest

from howl.operators import (
    BaseOperator, EqualOperator, GreaterThanOperator, LowerThanOperator, add_operator_type,
    get_operator_class)
from howl.tests.factories.observers import ObserverFactory


class TestOperatorBasics:

    def test_add_operator_type(self):
        class Mock():
            display_name = 'Mock operator'

        assert add_operator_type(Mock) is True

    @pytest.mark.parametrize('operator_class, return_value', [
        (EqualOperator, False),
        (GreaterThanOperator, False),
        (LowerThanOperator, False),
    ])
    def test_add_operator_type_not_in_registry(self, operator_class, return_value):

        assert add_operator_type(operator_class) is return_value

    @pytest.mark.parametrize('operator_class, return_value', [
        ('EqualOperator', EqualOperator),
        ('GreaterThanOperator', GreaterThanOperator),
        ('LowerThanOperator', LowerThanOperator),
    ])
    def test_get_operator_class(self, operator_class, return_value):
        get_operator_class(operator_class) == return_value

    def test_get_operator_class_not_exists(self):
        with pytest.raises(KeyError):
            get_operator_class('NotExists')


@pytest.mark.django_db
class TestBaseOperator:

    def test_compare_not_implemented(self):
        observer = ObserverFactory.create()
        with pytest.raises(NotImplementedError):
            BaseOperator(observer).compare(1)


@pytest.mark.django_db
class TestOperators:

    @pytest.mark.parametrize('operator_class, value, compare_value, return_value', [
        (EqualOperator, 49, 50, False),
        (EqualOperator, 50, 50, True),
        (EqualOperator, 51, 50, False),
        (GreaterThanOperator, 49, 50, False),
        (GreaterThanOperator, 50, 50, False),
        (GreaterThanOperator, 51, 50, True),
        (LowerThanOperator, 49, 50, True),
        (LowerThanOperator, 50, 50, False),
        (LowerThanOperator, 51, 50, False),
    ])
    def test_compare(self, operator_class, value, compare_value, return_value):
        observer = ObserverFactory.create(operator=operator_class.__name__, value=value)

        operator_class(observer).compare(value) is return_value
