# -*- coding: utf-8 -*-

from sqlalchemy.orm.mapper import configure_mappers

from flaskstarter import create_app
from flaskstarter.extensions import db
from flaskstarter.user import Users, ADMIN, USER, ACTIVE
from flaskstarter.tasks import MyTaskModel

application = create_app()


@application.cli.command("initdb")
def initdb():
    """Init/reset database."""

    db.drop_all()
    configure_mappers()
    db.create_all()

    # préparation de la base
