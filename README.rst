django-howl
===============

.. image:: https://badge.fury.io/py/django-howl.svg
    :target: https://badge.fury.io/py/django-howl

.. image:: https://travis-ci.org/deluge/django-howl.svg?branch=master
    :target: https://travis-ci.org/deluge/django-howl

.. image:: https://codecov.io/gh/deluge/django-howl/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/deluge/django-howl

.. image:: https://readthedocs.org/projects/django-howl/badge/?version=latest
  :target: http://django-howl.readthedocs.org/en/latest/?badge=latest
  :alt: Documentation Status


What is django-howl
-----------------------

`django-howl` is a Django app where you can add custom observers and use them to check almost everything you want and pushes alerts to signals. You can connect to the signals and handle it in your way like sending notifications over different APIs.


Requirements
------------

django-howl supports Python 3 only and requires at least Django 1.11.
If you need support for Django 1.8.x or 1.9.x have a look at django-howl < 1.0.0


Installation
============

* Install ``django-howl`` (or `download from PyPI <http://pypi.python.org/pypi/django-howl>`_):

.. code-block:: python

    pip install django-howl

* After Installation add it to ``INSTALLED_APPS`` in ``settings.py``:

.. code-block:: python

    INSTALLED_APPS = [
        # other apps
        'howl',
    ]


Usage
=====

Now you can login to the admin and configure some observers and build some nice apps
with it.


Prepare for development
-----------------------

A Python 3.6 interpreter is required in addition to pipenv.

.. code-block:: shell

    $ pipenv install --python 3.6 --dev


Now you're ready to run the tests:

.. code-block:: shell

    $ pipenv run py.test


Resources
=========

* `Documentation <https://django-howl.readthedocs.org/>`_
* `Bug Tracker <https://github.com/deluge/django-howl/issues>`_
* `Code <https://github.com/deluge/django-howl/>`_
