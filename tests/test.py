# -*- coding: utf-8 -*-

import pytest

from flask_login import current_user
from flaskstarter import create_app
from flaskstarter.extensions import db
from flaskstarter.user import Users, USER, ACTIVE


@pytest.fixture
def client():
    app = create_app()

    app.config["TESTING"] = True
    app.testing = True

    client = app.test_client()
    yield client


def test_liste_produits(client):
    response: dict = client.get("/")
    attendu = {
        "products": [
            {
                "name": "Brown eggs",
                "id": 1,
                "in_stock": true,
                "description": "Raw organic brown eggs in a basket",
                "price": 28.1,
                "weight": 400,
                "image": "0.jpg",
            },
            {
                "description": "Sweet fresh stawberry on the wooden table",
                "image": "1.jpg",
                "in_stock": true,
                "weight": 299,
                "id": 2,
                "name": "Sweet fresh stawberry",
                "price": 29.45,
            },
        ]
    }
    assert attendu == response.data, "test failed"
