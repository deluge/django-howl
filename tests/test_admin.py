import pytest
from django.contrib import admin

from howl.admin import AlertAdmin, ObserverAdmin
from howl.models import Alert, Observer


@pytest.mark.django_db
class TestObserverAdmin:
    def test_list_display(self, rf):
        modeladmin = ObserverAdmin(Observer, admin.site)
        assert modeladmin.list_display == ("name", "operator", "value")


@pytest.mark.django_db
class TestAlertAdmin:
    def test_list_display(self, rf):
        modeladmin = AlertAdmin(Alert, admin.site)
        assert modeladmin.list_display == ("identifier", "timestamp", "value", "state")
