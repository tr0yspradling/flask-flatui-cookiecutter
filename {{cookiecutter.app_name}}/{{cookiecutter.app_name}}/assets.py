# -*- coding: utf-8 -*-
"""Application assets."""
from flask_assets import Bundle, Environment

css = Bundle(
    'css/bootstrap.min.css',
    'css/bootstrap-grid.min.css',
    'css/flat-ui.min.css',
    'css/style.css',
    filters='cssmin',
    output='public/css/common.css'
)

js = Bundle(
    'js/jquery.min.js',
    'js/bootstrap.min.js',
    'js/plugins.js',
    'js/script.js',
    filters='jsmin',
    output='public/js/common.js'
)

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)
