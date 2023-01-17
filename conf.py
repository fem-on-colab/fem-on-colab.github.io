# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath("./_ext"))


# -- Project information -----------------------------------------------------

project = "FEM on Colab"
copyright = "2021-, Francesco Ballarin (and contributors)"
author = "Francesco Ballarin (and contributors)"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here.
extensions = [
    "ext"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
html_title = "FEM on Colab"

# The theme to use for HTML and HTML Help pages.
# From https://github.com/bashtage/sphinx-material
html_theme = "sphinx_material"

# Material theme options
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    "nav_title": "FEM on Colab",

    # Set you GA account ID to enable tracking
    "google_analytics_account": "UA-198305719-1",

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    "base_url": "https://fem-on-colab.github.io/",

    # Set the color and the accent color
    "theme_color": "#00325c",
    "color_primary": "unicatt",
    "color_accent": "unicatt",

    # Set the repo location to get a badge with stats
    "repo_url": "https://github.com/fem-on-colab/fem-on-colab/",
    "repo_name": "fem-on-colab",

    # Visible levels of the global TOC; -1 means unlimited
    "globaltoc_depth": 1,
    # If False, expand all TOC entries
    "globaltoc_collapse": True,
    # If True, show hidden TOC entries
    "globaltoc_includehidden": False,

    # Path to a touch icon, should be 152x152 or larger.
    "touch_icon": "images/fem-on-colab-logo.png",
    "logo_icon": "&#xe069",

    # Main menu links
    "nav_links": [
        {
            "href": "packages",
            "internal": True,
            "title": "Packages",
        },
        {
            "href": "contributing",
            "internal": True,
            "title": "How to contribute",
        },
        {
            "href": "citing",
            "internal": True,
            "title": "How to cite",
        }
    ],

    # Disable version dropbown
    "version_dropdown": False,
}
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom CSS files
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/jquery-dropdown/2.0.3/jquery.dropdown.min.css",
    "https://fonts.googleapis.com/css?family=Pangolin",
    "css/custom.css",
]

# Custom javascript files
html_js_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/jquery-dropdown/2.0.3/jquery.dropdown.min.js",
    "js/external_links.js"
]
