import pytest
from django.contrib import admin

from howl.admin import ObserverAdmin
from howl.models import Observer


@pytest.mark.django_db
class TestObserverAdmin:

    def test_get_readonly_fields(self, rf):
        modeladmin = ObserverAdmin(Observer, admin.site)
        assert modeladmin.list_display == ('name', 'operator', 'value')
