import pytest
import requests

from recipes_darya import app, db
from recipes_darya.modal.model import Dish


@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="session")
def preset():
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db_test.sqlite'
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()


@pytest.fixture(scope="session", autouse=True)
def empty_db():
    with app.app_context():
        db.drop_all()
        db.create_all()


def test_app(client):
    response = client.get("/api/dishes")
    data = response.get_json()
    assert type(data) == dict
    assert response.status_code == 200


def test_app_2(client):
    response = client.get("/api/dishe")
    data = response.get_json()
    # assert type(data) == dict
    assert response.status_code == 404


def test_create_dishes_ok(client, empty_db):
    response = client.post("/api/dishes", json={
        "name": "testing",
        "quantity": 15,
        "description": "some desc"
    })

    dish = Dish.query.filter_by(name="testing").first()
    dish_count = Dish.query.all()

    assert response.status_code == 200
    assert dish is not None
    assert len(dish_count) == 1


@pytest.mark.parametrize("input_value, expected_value", [
    ({
         "name": "testing",
         "description": "some desc"
     }, {
         "status": 400,
         "compare_with_none": False,
         "len": 1
     }),

    ({
         "name": "testing",
         "quantity": 15
     }, {
         "status": 400,
         "compare_with_none": False,
         "len": 1
     }),

    ({
         "name": "testing"
     }, {
         "status": 400,
         "compare_with_none": False,
         "len": 1
     }),

    ({
         "quantity": 15
     }, {
         "status": 400,
         "compare_with_none": False,
         "len": 1
     }),

    ({
         "quantity": 15,
         "description": "some desc"
     }, {
         "status": 400,
         "compare_with_none": False,
         "len": 1
     }),

    ({
         "description": "some desc"
     }, {
         "status": 400,
         "compare_with_none": False,
         "len": 1
     })
])
def test_create_dishes_fail_not_full_data(client, input_value, expected_value):
    response = client.post("/api/dishes", json=input_value)

    dish = Dish.query.filter_by(name="testing").first()
    dish_count = Dish.query.all()

    assert (dish is None) == expected_value["compare_with_none"]
    assert len(dish_count) == expected_value["len"]

    assert response.status_code == expected_value["status"]


def test_delete_dishes(client):
    response = client.post("/api/dishes", json={
        "name": "testing1",
        "quantity": 15,
        "description": "some desc"
    })

    dish = Dish.query.filter_by(name="testing1").first()
    assert response.json["status"] == 0
    assert response.status_code == 200
    assert dish is not None

    response = client.delete(f"/api/dishes/{response.json['data']['dishes']['id']}")
    dish_count = Dish.query.all()
    assert len(dish_count) == 1

    response = client.delete("/api/dishes/25")
    # respData = response.json
    assert response.json["status"] == 2
    assert response.status_code == 400


def test_update_dishes_ok(client):
    response = client.post("/api/dishes", json={
        "name": "testing3",
        "quantity": 15,
        "description": "some desc"
    })

    response = client.put(f"/api/dishes/{response.json['data']['dishes']['id']}", json={
        "name": "testing2",
        "quantity": 15,
        "description": "some desc"
    })
    dish = Dish.query.filter_by(name="testing2").first()
    assert response.status_code == 200
    dish_count = Dish.query.all()
    assert len(dish_count) == 2

    response = client.put("/api/dishes/20")
    assert response.json["status"] == 2
    assert response.status_code == 400
