import data
import pytest
import requests
import time

@pytest.fixture()
def create_user():
    url = f'{data.BASE_URL}/user'
    requests.post(url, headers=data.HEADERS_MINI, json=data.body_user)
    time.sleep(4)
    yield
    username = data.body_user['username']
    url = f'{data.BASE_URL}/user/{username}'
    requests.delete(url)

def test_get_user(create_user):
    username = data.body_user['username']
    url = f'{data.BASE_URL}/user/{username}'
    response_get = requests.get(url, headers=data.HEADERS_MINI)
    assert response_get.status_code == 200

def test_get_data_user(create_user):
    username = data.body_user['username']
    url = f'{data.BASE_URL}/user/{username}'
    response_get = requests.get(url, headers=data.HEADERS_MINI)
    assert response_get.json().get('username') == data.body_user['username']
    assert response_get.json().get('firstName') == data.body_user['firstName']
    assert response_get.json().get('lastName') == data.body_user['lastName']
    assert response_get.json().get('email') == data.body_user['email']
    assert response_get.json().get('phone') == data.body_user['phone']
    assert response_get.json().get('password') == data.body_user['password']

def test_get_incorrect_url():
    url = f'{data.BASE_URL}/usair/NoUsername'
    response_get = requests.get(url, headers=data.HEADERS_MINI)
    assert response_get.status_code == 404

def test_get_incorrect_username():
    url = f'{data.BASE_URL}/user/UniqUserNotFound'
    response_update = requests.get(url, headers=data.HEADERS_MINI)
    assert response_update.status_code == 404