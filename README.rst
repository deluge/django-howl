django-howl
===========

.. image:: https://badge.fury.io/py/django-howl.svg
    :target: https://badge.fury.io/py/django-howl

.. image:: https://github.com/deluge/django-howl/workflows/Testing/badge.svg?branch=master
    :target: https://github.com/deluge/django-howl/actions?query=workflow%3ATesting

.. image:: https://codecov.io/gh/deluge/django-howl/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/deluge/django-howl

.. image:: https://readthedocs.org/projects/django-howl/badge/?version=latest
  :target: http://django-howl.readthedocs.org/en/latest/?badge=latest
  :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
  :target: https://github.com/psf/black
  :alt: Code style: black


What is django-howl
-------------------

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

A Python 3 interpreter is required. If you use pyenv with a virtualenv, follow the next steps

.. code-block:: shell

    $ cd /path/to/project-root/
    $ mkvirtualenv django-howl
    # activate virtualenv, if not activated yet
    # and install all dev requirements:
    $ pip install -e .[dev]


Now you're ready to run the tests:

.. code-block:: shell

    $ py.test


Code style
----------

This project is styled by `black <https://github.com/psf/black/>` and `isort <https://github.com/timothycrosley/isort/>`. You can use the following command to format the code automatically and make it black and isort compatible:

.. code-block:: shell

    $ make format-python-code


Resources
=========

* `Documentation <https://django-howl.readthedocs.org/>`_
* `Bug Tracker <https://github.com/deluge/django-howl/issues>`_
* `Code <https://github.com/deluge/django-howl/>`_
