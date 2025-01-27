# -*- coding: utf-8 -*-

from flask import Flask

from .config import DefaultConfig
from .extensions import db


# For import *
__all__ = ['create_app']


def create_app(config=None, app_name=None):
    # Create a Flask app

    if app_name is None:
        app_name = DefaultConfig.PROJECT

    app = Flask(app_name,
                instance_relative_config=True)

    return app
