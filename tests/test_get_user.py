from types import NoneType

import pytest
import requests
import time

BASE_URL = 'https://petstore.swagger.io/v2'
HEADERS = {
    'accept': 'application/json',
}

data_body = {
    "id": 0, "username": "TestGetUserB", "password": "PASSWORD"
}

@pytest.fixture()
def create_user():
    url = f'{BASE_URL}/user'
    requests.post(url, headers=HEADERS, json=data_body)
    time.sleep(4)
    yield
    url = f'{BASE_URL}/user/{data_body["username"]}'
    requests.delete(url)

def test_get_0():
    url = f'{BASE_URL}/user/user1'
    response_update = requests.get(url, headers=HEADERS)
    assert response_update.status_code == 200

def test_get_1(create_user):
    username = data_body["username"]
    url = f'{BASE_URL}/user/{username}'
    response_update = requests.get(url, headers=HEADERS)
    assert response_update.status_code == 200

def test_get_2(create_user):
    url = f'{BASE_URL}/user/UniqUserNotFound'
    response_update = requests.get(url, headers=HEADERS)
    assert response_update.status_code == 404