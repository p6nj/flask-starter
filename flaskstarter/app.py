# -*- coding: utf-8 -*-

from flask import Flask


# For import *
__all__ = ['create_app']


def create_app(config=None, app_name=None):
    # Create a Flask app

    app = Flask(app_name,
                instance_relative_config=True)

    return app
