import os
from codecs import open

from setuptools import find_packages, setup


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION = __import__("howl").__version__


with open(os.path.join(BASE_DIR, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="django-howl",
    version=VERSION,
    description=(
        "Django app to observe almost everything you want and "
        "pushes notifications to signals."
    ),
    long_description=long_description,
    url="https://github.com/deluge/django-howl",
    project_urls={
        "Bug Reports": "https://github.com/deluge/django-howl/issues",
        "Source": "https://github.com/deluge/django-howl",
    },
    author="Benjamin Banduhn, Stephan Jaekel",
    author_email="deluge@banduhn.com",
    packages=find_packages(exclude=["examples", "docs", "tests", "tests.*"]),
    install_requires=["Django>=2.2,<3.3"],
    extras_require={"dev": [
        "coverage[toml]>=5.3",
        "factory-boy>=3.1.0",
        "freezegun>=1.0.0",
        "pytest>=6.1.1",
        "pytest-black>=0.3.12",
        "pytest-cov>=2.10.1",
        "pytest-django>=3.10.0",
        "pytest-flake8>=1.0.6",
        "pytest-isort>=1.2.0",
        "sphinx>=3.2.1",
        "sphinx-rtd-theme==0.5.0",
        "vcrpy>=4.1.1",
    ],},
    include_package_data=True,
    keywords="django howl observer watchdog alert signal",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
