Changelog
=========

0.1.13 - 2017-01-02
------------------

* refactor operator
* setting ``HOWL_OPERATOR_EXTENSIONS`` is renamed to ``HOWL_OPERATORS``


0.1.12 - 2017-01-01
------------------

* refactor operator extension registration
* extensions can added via ``HOWL_OPERATOR_EXTENSIONS`` setting


0.1.11 - 2016-04-09
------------------

* added missing kwargs to get_alert_identifier method in Alert.clear


0.1.10 - 2016-04-09
------------------

* change observer value from char field to float field to avoid some compare errors


0.1.9 - 2016-04-09
------------------

* added missing migration


0.1.8 - 2016-04-09
------------------

* change observer value from integer field to char field
* extend observer get_alert_identifier method with kwargs


0.1.7 - 2016-02-11
------------------

* This change includes a slight api change in the way how Alert.set and Alert.clear is called.
* In addtion, the way how waiting_period works is improved and more clear. A waiting_period of zero means immediate critical notification without warning.


0.1.6 - 2016-01-29
------------------

* extend Alert methods with kwargs and add compare_value to signals


0.1.5 - 2016-01-01
------------------

* adjust setup file


0.1.4 - 2016-01-01
------------------

* adjust setup file


0.1.3 - 2015-12-31
------------------

* adjust setup files and add apps.py


0.1.2 - 2015-12-19
------------------

* mini bugfixes.


0.1.1 - 2015-12-16
------------------

* Moved signal logic to Alert model.


0.1.0 - 2015-12-06
------------------

* Initial release.
