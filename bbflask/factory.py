# -*- coding: utf-8 -*-
from flask import Flask

from bbflask import settings
from bbflask.core import initialize_extensions
from bbflask.helpers import register_blueprints


def create_app(package_name):
    '''Create a `flask.Flask` app instance and return it.'''
    app = Flask(package_name)
    app.config.from_object(settings)

    # intitialize extensions since the app is configured now
    initialize_extensions(app)

    register_blueprints

    return app
