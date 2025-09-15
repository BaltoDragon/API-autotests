import data
import pytest
import requests
import time

@pytest.fixture()
def create_user_mini():
    url = f'{data.BASE_URL}/user'
    requests.post(url, headers=data.HEADERS_BASE, json=data.body_user_mini)
    time.sleep(4)
    yield
    username = data.body_user_mini['username']
    url = f'{data.BASE_URL}/user/{username}'
    requests.delete(url)

@pytest.fixture()
def create_user():
    url = f'{data.BASE_URL}/user'
    requests.post(url, headers=data.HEADERS_BASE, json=data.body_user)
    time.sleep(4)
    yield
    username = data.body_user['username']
    url = f'{data.BASE_URL}/user/{username}'
    requests.delete(url)

def test_update_new_data_single(create_user_mini):
    username = data.body_user_mini['username']
    update_data = data.update_data_single
    url = f'{data.BASE_URL}/user/{username}'
    response_update = requests.put(url, headers=data.HEADERS_BASE, json=update_data)
    assert response_update.status_code == 200

def test_update_new_data_multi(create_user_mini):
    username = data.body_user_mini['username']
    update_data = data.update_data_multi
    url = f'{data.BASE_URL}/user/{username}'
    response_update = requests.put(url, headers=data.HEADERS_BASE, json=update_data)
    assert response_update.status_code == 200

def test_update_change_data_single(create_user):
    username = data.body_user['username']
    update_data = data.update_data_single
    url = f'{data.BASE_URL}/user/{username}'
    response_update = requests.put(url, headers=data.HEADERS_BASE, json=update_data)
    assert response_update.status_code == 200

def test_update_change_data_multi(create_user):
    username = data.body_user['username']
    update_data = data.update_data_multi
    url = f'{data.BASE_URL}/user/{username}'
    response_update = requests.put(url, headers=data.HEADERS_BASE, json=update_data)
    assert response_update.status_code == 200

def test_update_array_data(create_user):
    username = data.body_user['username']
    update_data = data.update_data_array
    url = f'{data.BASE_URL}/user/{username}'
    response_update = requests.put(url, headers=data.HEADERS_BASE, json=update_data)
    assert response_update.status_code == 400

def test_update_incorrect_url():
    url = f'{data.BASE_URL}/usair/Username'
    response_update = requests.put(url, headers=data.HEADERS_BASE)
    assert response_update.status_code == 404

def test_update_without_data(create_user_mini):
    username = data.body_user['username']
    url = f'{data.BASE_URL}/user/{username}'
    response_update = requests.put(url, headers=data.HEADERS_BASE)
    assert response_update.status_code == 405