import pytest
import requests
import time

BASE_URL = 'https://petstore.swagger.io/v2'
HEADERS = {
    'accept': 'application/json',
}

data_body = {
        "id": 0, "username": "LoginUserAB", "firstName": "MyName",
        "email": "example@ex.com", "password": "PASSWORD"
    }

@pytest.fixture()
def create_user():
    url = f'{BASE_URL}/user'
    requests.post(url, headers=HEADERS, json=data_body)
    time.sleep(4)
    yield
    url = f'{BASE_URL}/user/{data_body["username"]}'
    requests.delete(url)

def test_login_1(create_user):
    login = data_body["username"]
    pwd = data_body["password"]
    url = f'{BASE_URL}/user/login?username={login}&password={pwd}'
    response_login = requests.get(url, headers=HEADERS)
    assert response_login.status_code == 200
    url = f'{BASE_URL}/user/logout'
    responce_logout = requests.get(url, headers=HEADERS)
    assert responce_logout.status_code == 200

def test_login_fail_1(create_user):
    login = data_body["username"]
    pwd = "bad_password"
    url = f'{BASE_URL}/user/login?username={login}&password={pwd}'
    response_update = requests.get(url, headers=HEADERS)
    assert response_update.status_code == 400

def test_login_fail_2(create_user):
    login = "bad_username"
    pwd = data_body["password"]
    url = f'{BASE_URL}/user/login?username={login}&password={pwd}'
    response_update = requests.get(url, headers=HEADERS)
    assert response_update.status_code == 400