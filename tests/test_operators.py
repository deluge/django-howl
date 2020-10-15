import pytest

from howl.operators import (
    BaseOperator,
    EqualOperator,
    GreaterThanOperator,
    LowerThanOperator,
)
from tests.factories.observers import ObserverFactory


@pytest.mark.django_db
class TestBaseOperator:
    def test_compare_not_implemented(self):
        observer = ObserverFactory.create()
        with pytest.raises(NotImplementedError):
            BaseOperator(observer).compare(1)


@pytest.mark.django_db
class TestOperators:
    @pytest.mark.parametrize(
        "operator_class, value, compare_value, return_value",
        [
            (EqualOperator, "49", "50", False),
            (EqualOperator, "50", "50", True),
            (EqualOperator, "50", 50.0, True),
            (EqualOperator, "51", "50", False),
            (GreaterThanOperator, "49", 50, False),
            (GreaterThanOperator, "50", 50, False),
            (GreaterThanOperator, "51", 50, True),
            (GreaterThanOperator, 51.5, 50, True),
            (LowerThanOperator, "49", "50", True),
            (LowerThanOperator, 49.5, "50.5", True),
            (LowerThanOperator, "50", "50", False),
            (LowerThanOperator, "51", "50", False),
        ],
    )
    def test_compare(self, operator_class, value, compare_value, return_value):
        observer = ObserverFactory.create(operator=operator_class.__name__, value=value)

        operator_class(observer).compare(value) is return_value
