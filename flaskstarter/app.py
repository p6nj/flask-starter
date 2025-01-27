# -*- coding: utf-8 -*-

from flask import Flask

from .config import DefaultConfig
from .user import Users, UsersAdmin
from .settings import settings
from .tasks import tasks, MyTaskModelAdmin
from .frontend import frontend, ContactUsAdmin
from .extensions import db, mail, cache, login_manager, admin
from .utils import INSTANCE_FOLDER_PATH, pretty_date


# For import *
__all__ = ['create_app']


def create_app(config=None, app_name=None):
    # Create a Flask app

    if app_name is None:
        app_name = DefaultConfig.PROJECT

    app = Flask(app_name,
                instance_path=INSTANCE_FOLDER_PATH,
                instance_relative_config=True)

    return app
