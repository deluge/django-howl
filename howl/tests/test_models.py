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
        (49, 50, False, 1),
        (50, 50, True, 0),
        (51, 50, False, 1),
    ])
    def test_compare(self, value, compare_value, return_value, count_objects):
        obj = ObserverFactory.create(value=value)

        assert Alert.objects.all().count() == 0
        assert obj.compare(compare_value) is return_value
        assert Alert.objects.all().count() == count_objects


@pytest.mark.django_db
class TestAlertModel:

    def test_repr(self, activate_en):
        observer = ObserverFactory.create(name='my observer')
        obj = AlertFactory.create(id=23, observer=observer)

        assert str(obj) == 'Alert (ID: 23) for my observer'

    @mock.patch('howl.models.alert_wait.send')
    def test_warn(self, mock):
        observer = ObserverFactory.create(value=4, waiting_period=0)
        Alert.set(observer, 2)

        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_WAITING
        assert mock.call_count == 1

    @mock.patch('howl.models.alert_notify.send')
    def test_warn_critical_waiting_priod_not_achieved(self, mock):
        observer = ObserverFactory.create(value=4, waiting_period=5)
        AlertFactory.create(observer=observer)
        Alert.set(observer, 2)

        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_WAITING
        assert mock.call_count == 0

    @mock.patch('howl.models.alert_notify.send')
    def test_warn_critical(self, mock):
        observer = ObserverFactory.create(value=4, waiting_period=0)
        AlertFactory.create(observer=observer, state=Alert.STATE_WAITING)

        Alert.set(observer, 2)

        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_NOTIFIED
        assert mock.call_count == 1

    @mock.patch('howl.models.alert_notify.send')
    def test_warn_notified(self, mock):
        observer = ObserverFactory.create(value=4, waiting_period=0)
        AlertFactory.create(observer=observer, state=Alert.STATE_NOTIFIED)
        Alert.set(observer, 2)

        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_NOTIFIED
        assert mock.call_count == 0

    @mock.patch('howl.models.alert_notify.send')
    def test_warn_every_time(self, mock):
        observer = ObserverFactory.create(value=4, waiting_period=0, alert_every_time=True)
        AlertFactory.create(observer=observer, state=Alert.STATE_NOTIFIED)

        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_NOTIFIED
        assert mock.call_count == 0

        Alert.set(observer, 2)

        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_NOTIFIED
        assert mock.call_count == 1

    @mock.patch('howl.models.alert_clear.send')
    def test_clear(self, mock):
        observer = ObserverFactory.create()
        AlertFactory.create(observer=observer)
        Alert.clear(observer)

        assert Alert.objects.all().count() == 0
        assert mock.call_count == 1

    @mock.patch('howl.models.alert_clear.send')
    def test_clear_no_object(self, mock):
        observer = ObserverFactory.create()
        Alert.clear(observer)

        assert Alert.objects.all().count() == 0
        assert mock.call_count == 0
