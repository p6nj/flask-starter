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
                "description": " organic brown eggs in a basket",
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

def test_Nouvelle_Commande(client):
    response: dict = client.post("/order",
    attendu = {
        "product": { "id": 123, "quantity": 2 }
    })
    # assert attendu == response.data, "missing-fields"
    assert response.status_code == 302, "La commande devrait être créée avec un status 302"
    assert "Location" in response.headers, "La réponse doit contenir l'en-tête 'Location'"

def test_Commande_Sans_Produit(client):
    # Envoi d'une requête vide (erreur attendue)
    response = client.post("/order", json={})

    # Vérification du code de statut et du message d'erreur attendu
    assert response.status_code == 422, "L'API devrait retourner une erreur 422 si 'product' est manquant"
    assert response.json == {
        "errors": {
            "product": {
                "code": "missing-fields",
                "name": "La création d'une commande nécessite un produit"
            }
        }
    }, "Le message d'erreur retourné est incorrect"

def test_Commande_Produit_Hors_Stock(client):
    # Supposons que le produit 999 est hors stock
    response = client.post("/order", json={
        "product": { "id": 999, "quantity": 1 }
    })

    # Vérification du code de statut et du message d'erreur attendu
    assert response.status_code == 422, "L'API devrait retourner une erreur 422 si le produit n'est pas en stock"
    assert response.json == {
        "errors": {
            "product": {
                "code": "out-of-inventory",
                "name": "Le produit demandé n'est pas en inventaire"
            }
        }
    }, "Le message d'erreur retourné est incorrect"

    