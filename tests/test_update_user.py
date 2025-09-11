import pytest
import requests
import time

BASE_URL = 'https://petstore.swagger.io/v2'
HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

data_body = {
    "id": 0, "username": "TestUpdateUserAB", "password": "PASSWORD"
}

data_update_1 = {"email": "example@ex.com"}

data_update_2 = {"lastName": "MyLastName", "phone": "1234567890",}

@pytest.fixture()
def create_user():
    url = f'{BASE_URL}/user'
    requests.post(url, headers=HEADERS, json=data_body)
    time.sleep(4)
    yield
    url = f'{BASE_URL}/user/{data_body["username"]}'
    requests.delete(url)


def test_update_1(create_user):
    username = data_body["username"]
    url = f'{BASE_URL}/user/{username}'
    response_update = requests.put(url, headers=HEADERS, json=data_update_1)
    assert response_update.status_code == 200

def test_update_2(create_user):
    username = data_body["username"]
    url = f'{BASE_URL}/user/{username}'
    response_update = requests.put(url, headers=HEADERS, json=data_update_2)
    assert response_update.status_code == 200