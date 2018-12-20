# -*- coding: utf-8 -*-
"""Create an application instance."""
import argparse
from flask.helpers import get_debug_flag
from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)

if __name__ == '__main__':
    app.run(port=8080)
