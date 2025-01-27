# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_caching import Cache
from flask_login import LoginManager
from flask_admin import Admin, AdminIndexView
from flask_admin.menu import MenuLink


db = SQLAlchemy()

cache = Cache()
