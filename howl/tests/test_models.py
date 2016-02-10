import mock
import pytest

from howl.models import Alert
from howl.tests.factories.observers import AlertFactory, ObserverFactory


@pytest.mark.django_db
class TestObserverModel:

    def test_repr(self):
        obj = ObserverFactory.create(name='test observer')

        assert str(obj) == 'test observer'

    def test_alert_identifier(self):
        obj = ObserverFactory.create(name='test observer')
        assert obj.get_alert_identifier() == 'howl-observer:{0}'.format(obj.pk)

    @pytest.mark.parametrize('value, compare_value, count_objects', [
        (49, 50, 1),
        (50, 50, 0),
        (51, 50, 1),
    ])
    def test_get_alert(self, value, compare_value, count_objects):
        obj = ObserverFactory.create(value=value)

        assert Alert.objects.all().count() == 0
        alert = obj.get_alert(compare_value)
        assert Alert.objects.all().count() == count_objects

        if alert:
            assert alert == Alert.objects.first()

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
        obj = AlertFactory.create(id=23, identifier=observer.get_alert_identifier())

        assert str(obj) == 'Alert for howl-observer:{0}'.format(observer.pk)

    def test_set_observer_and_identifier_missing(self):
        with pytest.raises(ValueError):
            Alert.set(2)

    def test_clear_observer_and_identifier_missing(self):
        with pytest.raises(ValueError):
            Alert.clear(2)

    @mock.patch('howl.models.alert_notify.send')
    def test_no_warning_period(self, mock):
        observer = ObserverFactory.create(value=4, waiting_period=0)
        Alert.set(2, observer=observer)

        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_NOTIFIED
        assert mock.call_count == 1

    @mock.patch('howl.models.alert_wait.send')
    def test_warn_observer(self, mock):
        observer = ObserverFactory.create(value=4, waiting_period=5)
        Alert.set(2, observer=observer)

        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_WAITING
        assert mock.call_count == 1

    @mock.patch('howl.models.alert_notify.send')
    def test_warn_critical_waiting_priod_not_achieved(self, mock):
        observer = ObserverFactory.create(value=4, waiting_period=5)
        AlertFactory.create(identifier=observer.get_alert_identifier())
        Alert.set(2, observer=observer)

        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_WAITING
        assert mock.call_count == 0

    @mock.patch('howl.models.alert_notify.send')
    def test_warn_critical_observer(self, mock):
        observer = ObserverFactory.create(value=4, waiting_period=0)
        AlertFactory.create(
            identifier=observer.get_alert_identifier(), state=Alert.STATE_WAITING)

        Alert.set(2, observer=observer)

        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_NOTIFIED
        assert mock.call_count == 1

    @mock.patch('howl.models.alert_notify.send')
    def test_warn_notified_observer(self, mock):
        observer = ObserverFactory.create(value=4, waiting_period=0)
        AlertFactory.create(
            identifier=observer.get_alert_identifier(), state=Alert.STATE_NOTIFIED)
        Alert.set(2, observer=observer)

        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_NOTIFIED
        assert mock.call_count == 0

    @mock.patch('howl.models.alert_notify.send')
    def test_warn_every_time(self, mock):
        observer = ObserverFactory.create(
            value=4, waiting_period=0, alert_every_time=True)
        AlertFactory.create(
            identifier=observer.get_alert_identifier(), state=Alert.STATE_NOTIFIED)

        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_NOTIFIED
        assert mock.call_count == 0

        Alert.set(2, observer=observer)

        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_NOTIFIED
        assert mock.call_count == 1

    @mock.patch('howl.models.alert_wait.send')
    def test_warn_identifier(self, mock):
        Alert.set(2, identifier='alert-name', waiting_period=5)

        assert Alert.objects.all().count() == 1
        alert = Alert.objects.first()
        assert alert.state == Alert.STATE_WAITING
        assert alert.identifier == 'alert-name'
        assert mock.call_count == 1

    @mock.patch('howl.models.alert_notify.send')
    def test_warn_critical_identifier(self, mock):
        alert = AlertFactory.create(state=Alert.STATE_WAITING)
        Alert.set(identifier=alert.identifier)

        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_NOTIFIED
        assert mock.call_count == 1

    @mock.patch('howl.models.alert_notify.send')
    def test_warn_notified_identifier(self, mock):
        alert = AlertFactory.create(state=Alert.STATE_NOTIFIED)
        Alert.set(identifier=alert.identifier)

        assert Alert.objects.all().count() == 1
        assert Alert.objects.first().state == Alert.STATE_NOTIFIED
        assert mock.call_count == 0

    @mock.patch('howl.models.alert_clear.send')
    def test_clear_observer(self, mock):
        observer = ObserverFactory.create()
        AlertFactory.create(identifier=observer.get_alert_identifier())
        Alert.clear(observer.value, observer=observer)

        assert Alert.objects.all().count() == 0
        assert mock.call_count == 1

    @mock.patch('howl.models.alert_clear.send')
    def test_clear_identifier(self, mock):
        alert = AlertFactory.create()
        Alert.clear(identifier=alert.identifier)

        assert Alert.objects.all().count() == 0
        assert mock.call_count == 1

    @mock.patch('howl.models.alert_clear.send')
    def test_clear_no_object(self, mock):
        observer = ObserverFactory.create()
        Alert.clear(observer.value, observer=observer)

        assert Alert.objects.all().count() == 0
        assert mock.call_count == 0
