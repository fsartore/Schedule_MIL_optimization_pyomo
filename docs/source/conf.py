# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# conf.py

import os
import sys

# Add the directory containing functions to the system path
sys.path.insert(0, os.path.abspath('../../'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MIL Schedule Optimization Pyomo'
copyright = '2024, Federico Sartore'
author = 'Federico Sartore'
release = '0.1'



# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.duration",
    "sphinx.ext.autosectionlabel",
    "nbsphinx",                    # Myst
    "sphinx.ext.autodoc",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'furo'         # sphinx theme gallery for more
html_theme = 'sphinx_rtd_theme'         # sphinx theme gallery for more
html_static_path = ['_static']
