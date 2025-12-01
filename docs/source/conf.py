import os
import sys
import sphinx_rtd_theme


sys.path.insert(0, os.path.abspath('../../'))

project = 'Workit'
copyright = '2025, Totti'
author = 'Totti'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinxcontrib.mermaid',
    'sphinx_rtd_theme'
]

templates_path = ['_templates']
language = 'es'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
