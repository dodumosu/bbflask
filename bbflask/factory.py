# -*- coding: utf-8 -*-
from flask import Flask

from bbflask import settings


def create_app():
    '''Create a `flask.Flask` app instance and return it.'''
    app = Flask(settings.PROJECT_NAME)
    app.config.from_object(settings)

    return app
