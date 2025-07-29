# Configuration file for the Sphinx documentation builder.

project = 'CentreStack Admin Guide'
author = 'Gladinet'

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autosectionlabel',
]

# Paths that contain templates, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files
# and directories to ignore when looking for source files.
exclude_patterns = []

# The master toctree document.
root_doc = 'index'

# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_rtd_theme'

# Paths that contain custom static files, such as style sheets.
html_static_path = ['_static']
