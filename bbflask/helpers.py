# -*- coding: utf-8 -*-
from flask import Blueprint

from bbflask import blueprints


def register_blueprints(app):
    '''Searches for `flask.Blueprint` instances defined in the
    top-level blueprints module and registers them on the app.'''
    for item in dir(blueprints):
        item = getattr(blueprints, item)

        if isinstance(item, Blueprint):
            app.register_blueprint(item)
