import pytest
import json
from urllib.parse import urlencode

from app.app import app

with open("./users.json", "r") as f:
    users = json.load(f)


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_get_users(client):
    res = client.get('/users')
    data = res.get_json()
    assert res.status_code == 200
    assert data == users


def test_get_user_by_id(client):
    test_data = [
        {"name": "geralt", "is_success": True},
        {"name": "lara_croft", "is_success": True},
        {"name": "mario", "is_success": True},
        {"name": "gordon_freeman", "is_success": True},
        {"name": "unknown", "is_success": False},
    ]
    for td in test_data:
        res = client.get('/users/{}'.format(td["name"]))
        data = res.get_json()
        if td["is_success"]:
            assert res.status_code == 200
            assert data == users[td["name"]]
        else:
            assert res.status_code == 500


def test_arithmetic(client):
    error_dict_key = "status"
    error_400 = "400 Bad Request: The browser (or proxy) sent a request that this server could not understand."
    error_div_by_zero = "division by zero"
    data_keys = ["x", "y", "operation"]

    test_data = [
        # Invalid input
        {"is_success": False, "error": error_400},
        {"x": 2, "is_success": False, "error": error_400},
        {"y": 3, "is_success": False, "error": error_400},
        {"x": "a", "y": "b", "is_success": False, "error": error_400},
        {"x": 2, "y": "b", "is_success": False, "error": error_400},
        {"x": "a", "y": 3, "is_success": False, "error": error_400},
        # Valid input
        {"x": 4, "y": 2, "is_success": True, "expected": 6},
        {"x": 4, "y": 2, "operation": "+", "is_success": True, "expected": 6},
        {"x": 4, "y": 2, "operation": "-", "is_success": True, "expected": 2},
        {"x": 4, "y": 2, "operation": "/", "is_success": True, "expected": 2},
        {"x": 4, "y": 2, "operation": "*", "is_success": True, "expected": 8},
        {"x": 4, "y": 0, "operation": "/",
            "is_success": False, "error": error_div_by_zero},
    ]
    for td in test_data:
        res = client.post(
            '/arithmetic?{}'.format(urlencode({key: td.get(key, None) for key in td if key in data_keys})))
        data = res.get_json()
        if td["is_success"]:
            assert data["results"] == td["expected"]
        else:
            assert data[error_dict_key] is not None
            assert data[error_dict_key] == td["error"]
