import pytest
from django.utils.translation import activate as activate_language


@pytest.fixture()
def activate_en():
    activate_language('en')
