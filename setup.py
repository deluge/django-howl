import os
from codecs import open

from setuptools import find_packages, setup


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION = __import__('howl').__version__


with open(os.path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


dev_require = [
    'factory-boy>=2.11',
    'pytest>=5.4.1',
    'pytest-black>=0.3.8',
    'pytest-cov>=2.8.1',
    'pytest-django>=3.8.0',
    'pytest-flake8>=1.0.4',
    'pytest-isort>=0.3.1',
    'sphinx>=2.4.4',
    'sphinx-rtd-theme==0.4.3',
    'freezegun>=0.3',
    'vcrpy>=2.1.0'
]


setup(
    name='django-howl',
    version=VERSION,
    description=(
        'Django app to observe almost everything you want and '
        'pushes notifications to signals.'
    ),
    long_description=long_description,
    url='https://github.com/deluge/django-howl',
    project_urls={
        'Bug Reports': 'https://github.com/deluge/django-howl/issues',
        'Source': 'https://github.com/deluge/django-howl',
    },
    author='Benjamin Banduhn, Stephan Jaekel',
    author_email='deluge@banduhn.com',
    packages=find_packages(exclude=['examples', 'docs', 'tests', 'tests.*']),
    install_requires=['Django>=1.11,<2.3'],
    extras_require={
        'dev': dev_require,
    },
    include_package_data=True,
    keywords='django howl observer watchdog alert signal',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
