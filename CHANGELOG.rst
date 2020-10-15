*********
Changelog
*********

1.1.x
=====

1.1.0 - 2020-10-15
------------------

* add support for python 3.9
* add support for django 3.0 and 3.1
* drop support for python < 3.6
* drop support for django < 2.2


1.0.x
=====

1.0.5 - 2020-03-15
------------------

* add support for python 3.7 and 3.8
* update Pipfile.lock and test environment to avoid security issues
* use github actions


1.0.4 - 2019-06-25
------------------

* increase Django version
* update Pipfile.lock and test environment to avoid security issues


1.0.3 - 2019-03-30
------------------

* add more documentation


1.0.2 - 2019-02-15
------------------

* increase test coverage
* update requirements and dev packages
* use flake8 instead of pep8 and flakes


1.0.1 - 2018-12-08
------------------

* Fix: add missing on_delete argument to migration


1.0.0 - 2018-12-07
------------------

* drop support for django < 1.11
* add support for django 2.x


0.1.x
=====

0.1.13 - 2017-01-02
-------------------

* refactor operator
* setting ``HOWL_OPERATOR_EXTENSIONS`` is renamed to ``HOWL_OPERATORS``


0.1.12 - 2017-01-01
-------------------

* refactor operator extension registration
* extensions can added via ``HOWL_OPERATOR_EXTENSIONS`` setting


0.1.11 - 2016-04-09
-------------------

* added missing kwargs to get_alert_identifier method in Alert.clear


0.1.10 - 2016-04-09
-------------------

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
