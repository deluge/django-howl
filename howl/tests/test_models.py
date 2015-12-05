import time

import mock
import pytest

from howl.models import Alert
from howl.tests.factories.observers import AlertFactory, ObserverFactory


@pytest.mark.django_db
class TestObserverModel:

    def test_repr(self):
        obj = ObserverFactory.create(name='test observer')

        assert str(obj) == 'test observer'

    @pytest.mark.parametrize('value, compare_value, return_value, count_objects', [
        (49, 50, True, 1),
        (50, 50, False, 0),
        (51, 50, True, 1),
    ])
    def test_alert(self, value, compare_value, return_value, count_objects):
        obj = ObserverFactory.create(value=value)

        assert Alert.objects.all().count() == 0
        assert obj.alert(compare_value) is return_value
        assert Alert.objects.all().count() == count_objects

    @mock.patch('howl.models.howl_alert_delete.send')
    def test_alert_delete(self, mock):
        obj = ObserverFactory.create(value=4)
        obj.alert(3)
        assert Alert.objects.all().count() == 1
        time.sleep(0.5)
        obj.alert(4)
        assert Alert.objects.all().count() == 0
        assert mock.call_count == 1

    @mock.patch('howl.models.howl_alert_critical.send')
    def test_alert_critical(self, mock):
        obj = ObserverFactory.create(value=4)
        obj.alert(3)
        assert Alert.objects.all().count() == 1
        time.sleep(0.5)
        obj.alert(3)
        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_NOTIFIED
        assert mock.call_count == 1

    @mock.patch('howl.models.howl_alert_critical.send')
    def test_alert_critical_every_time(self, mock):
        obj = ObserverFactory.create(value=4, alert_every_time=True)
        obj.alert(3)
        assert Alert.objects.all().count() == 1
        time.sleep(0.5)
        obj.alert(3)
        time.sleep(0.5)
        obj.alert(3)
        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_NOTIFIED
        assert mock.call_count == 2

    @mock.patch('howl.models.howl_alert_warn.send')
    def test_alert_waiting_priod_not_achieved(self, mock):
        obj = ObserverFactory.create(value=4, waiting_period=5)
        obj.alert(3)
        assert Alert.objects.all().count() == 1
        time.sleep(0.5)
        obj.alert(3)
        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_WAITING
        assert mock.call_count == 1


@pytest.mark.django_db
class TestAlertModel:

    def test_repr(self, activate_en):
        observer = ObserverFactory.create(name='my observer')
        obj = AlertFactory.create(id=23, observer=observer)

        assert str(obj) == 'Alert (ID: 23) for my observer'
