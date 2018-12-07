import os
from codecs import open

from setuptools import setup, find_packages


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION = __import__('howl').__version__


with open(os.path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django-howl',
    version=VERSION,
    description='Django app to provide notifications in several ways',
    long_description=long_description,
    url='https://github.com/deluge/django-howl',
    project_urls={
        'Bug Reports': 'https://github.com/deluge/django-howl/issues',
        'Source': 'https://github.com/deluge/django-howl',
    },
    author='Benjamin Banduhn, Stephan Jaekel',
    author_email='deluge@banduhn.com',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=['Django>=1.11,<2.2'],
    include_package_data=True,
    keywords='django howl',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
