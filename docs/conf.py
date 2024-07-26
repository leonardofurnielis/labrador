# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
from pathlib import Path

project = 'spyder-index'
copyright = '2024, Leonardo Furnielis'
author = 'Leonardo Furnielis'
release = '0.2.7'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

"""Setup project path for sphinx and verify that it's valid"""
for idx, dir in enumerate(["../"]):
    src_dir = Path(os.path.abspath(dir))
    if not src_dir.exists():
        raise Exception(f"Provided project directory '{src_dir}' does not exists!")

    sys.path.insert(idx, str(src_dir.absolute()))

extensions = [
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.idea']

# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autoclass_content

autoclass_content = "class"
autodoc_typehints = "description"
autodoc_typehints_format = "short"
autodoc_class_signature = "separated"
autodoc_default_options = {"exclude-members": "__init__"}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_title = "🕸️ spyder-index Framework"
html_copy_source = False
html_show_sourcelink = False
