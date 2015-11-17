import os

from setuptools import find_packages, setup


VERSION = '0.1.0'


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with open(filename) as fp:
        return fp.read()


tests_require = [
    'coverage',
    'pytest',
    'pytest-cov',
    'pytest-pep8',
    'pytest-flakes',
    'pytest-isort',
    'pytest-django',
    'factory-boy',
]


setup(
    name='django-howl',
    description='Django app to provide notifications in several ways',
    long_description=read('README.rst'),
    version=VERSION,
    license='BSD',
    author='Benjamin Banduhn, Stephan Jaekel',
    author_email='deluge@banduhn.com',
    url='http://github.com/deluge/django-howl/',
    packages=find_packages(exclude=[
        'howl.tests',
        'howl.tests.factories',
    ]),
    test_suite='.',
    tests_require=tests_require,
    install_requires=[
        'Django>=1.8,<1.10',
    ],
    extras_require={
        'tests': tests_require,
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Framework :: Django',
    ],
)
