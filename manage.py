# -*- coding: utf-8 -*-

from peewee import Model

from flaskstarter import create_app
from flaskstarter.extensions import db

application = create_app()


@application.cli.command("initdb")
def initdb():
    """Init/reset database."""
    db.create_tables(Model.__subclasses__())

    # préparation de la base
