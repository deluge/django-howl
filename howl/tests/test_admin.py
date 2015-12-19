import pytest
from django.contrib import admin

from howl.admin import AlertAdmin, ObserverAdmin
from howl.models import Alert, Observer
from howl.tests.factories.observers import AlertFactory, ObserverFactory


@pytest.mark.django_db
class TestObserverAdmin:

    def test_list_display(self, rf):
        modeladmin = ObserverAdmin(Observer, admin.site)
        assert modeladmin.list_display == ('name', 'operator', 'value')


@pytest.mark.django_db
class TestAlertAdmin:

    def test_list_display(self, rf):
        modeladmin = AlertAdmin(Alert, admin.site)
        assert modeladmin.list_display == ('get_observer_name', 'timestamp', 'value', 'state')

    def test_get_observer_name(self, rf):
        observer = ObserverFactory.create()
        alert = AlertFactory.create(observer=observer)

        modeladmin = AlertAdmin(Alert, admin.site)
        assert modeladmin.get_observer_name(alert) == observer.name
