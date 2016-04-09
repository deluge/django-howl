#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys


sys.path.append(os.path.abspath('.'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_settings')

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'django-howl'
copyright = 'Benjamin Banduhn'
version = '0.1.10'
release = '0.1.10'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
# html_static_path = ['_static']
htmlhelp_basename = 'howldoc'
latex_documents = [(
    'index', 'howl.tex', 'django-howl Documentation', 'Benjamin Banduhn', 'manual')]

man_pages = [('index', 'howl', 'django-howl Documentation', ['Benjamin Banduhn'], 1)]

texinfo_documents = [(
    'index', 'howl', 'django-howl Documentation',
    'Benjamin Banduhn', 'django-howl', 'Generate thumbnails of anything.', 'Miscellaneous'
)]

intersphinx_mapping = {'http://docs.python.org/': None}
