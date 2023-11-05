import pytest
import requests

from recipes_darya import app, db
from recipes_darya.modal.model import Ingredient


@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="session")
def preset():
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db_test.sqlite'


@pytest.fixture(scope="session", autouse=True)
def empty_db():
    with app.app_context():
        db.drop_all()
        db.create_all()


def test_get_all(client):
    response = client.get("/api/ingredients")
    data = response.get_json()
    assert type(data) == dict
    assert response.status_code == 200


def test_create_ingredients_ok(client):
    response = client.post("/api/ingredients", json={
        "name": "test",
        "protein": 2,
        "fat": 3,
        "carb": 4,
        "calories": 5
    })

    item = Ingredient.query.filter_by(name="test").first()
    item_count = Ingredient.query.all()

    assert response.status_code == 200
    assert item is not None
    assert len(item_count) == 1


def test_create_ingredients_fail(client):
    response = client.post("/api/ingredients", json={
        "name": "test",
        "protein": 2,
        "fat": 3,
        "carb": 4,
        "calories": 5
    })

    assert response.status_code == 400
    assert response.json["description"] == "Name already exist"

    response = client.post("/api/ingredients", json={
        "protein": 3,
        "fat": 4,
        "carb": 5,
        "calories": 6
    })

    item_count = Ingredient.query.all()

    assert response.status_code == 400
    assert response.json["status"] == 1
    assert len(item_count) == 1


def test_delete_ingredients(client):
    response = client.post("/api/ingredients", json={
        "name": "test2",
        "protein": 5,
        "fat": 6,
        "carb": 7,
        "calories": 8
    })

    item = Ingredient.query.filter_by(name="test2").first()
    assert item is not None
    assert response.json["status"] == 0
    assert response.status_code == 200

    response = client.delete(f"/api/ingredients/{response.json['data']['ingredients']['id']}")
    item_count = Ingredient.query.all()
    assert len(item_count) == 1

    response = client.delete("/api/ingredients/22")
    assert response.json["description"] == "Fail"
    assert response.status_code == 400

def test_update_ingredients(client):
    response = client.post("/api/ingredients", json={
        "name": "test3",
        "protein": 7,
        "fat": 8,
        "carb": 9,
        "calories": 10
    })

    response = client.put(f"/api/ingredients/{response.json['data']['ingredients']['id']}", json={
        "name": "test4",
        "protein": 3,
        "fat": 4,
        "carb": 5,
        "calories": 8
    })

    item = Ingredient.query.filter_by(name="test4").first()
    assert response.status_code == 200
    item_count = Ingredient.query.all()
    assert len(item_count) == 2

    response = client.put("/api/ingredients/17")
    assert response.status_code == 400
    assert response.json["status"] == 2
