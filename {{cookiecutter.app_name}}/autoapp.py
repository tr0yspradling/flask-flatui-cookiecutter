# -*- coding: utf-8 -*-
"""Create an application instance."""
import argparse
from flask.helpers import get_debug_flag
from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)

def run(app, default_host="127.0.0.1",
             default_port="5000"):
    """
    Takes a flask.Flask instance and runs it. Parses
    command-line flags to configure the app.
    """

    # Set up the command-line options
    parser = argparse.Ar()
    parser.add_option("-H", "--host",
                      help="Hostname of the Flask app " + \
                           "[default %s]" % default_host,
                      default=default_host)
    parser.add_option("-P", "--port",
                      help="Port for the Flask app " + \
                           "[default %s]" % default_port,
                      default=default_port)
    # Two options useful for debugging purposes, but
    # a bit dangerous so not exposed in the help message.
    parser.add_option("-d", "--debug",
                      action="store_true", dest="debug",
                      help=argparse.SUPPRESS)
    parser.add_option("-p", "--profile",
                      action="store_true", dest="profile",
                      help=argparse.SUPPRESS)
    options, _ = parser.parse_args()
    app.run(
        debug=options.debug,
        host=options.host,
        port=int(options.port)
    )

if __name__ == '__main__':
    run(app, default_port=8080)
