import pytest
from recipes_darya import app
import requests


def test_ok():
    a = 10
    assert a == 10, "Not equal"


def test_fail():
    a = 5
    assert a != 10, "Not equal"


def test_url_ok():
    response = requests.get("https://google.com")
    assert response.status_code == 200, "FAIL"


@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


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

