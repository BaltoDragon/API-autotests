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

def test_login_logout(create_user):
    login = data.body_user['username']
    pwd = data.body_user['password']
    url = f'{data.BASE_URL}/user/login?username={login}&password={pwd}'
    response_login = requests.get(url, headers=data.HEADERS_MINI)
    assert response_login.status_code == 200
    url = f'{data.BASE_URL}/user/logout'
    responce_logout = requests.get(url, headers=data.HEADERS_MINI)
    assert responce_logout.status_code == 200

def test_login_incorrect_url():
    login = data.body_user['username']
    pwd = data.body_user['password']
    url = f'{data.BASE_URL}/usair/login?username={login}&password={pwd}'
    response_login = requests.get(url, headers=data.HEADERS_MINI)
    assert response_login.status_code == 404

def test_login_incorrect_password(create_user):
    login = data.body_user['username']
    pwd = "bad_password"
    url = f'{data.BASE_URL}/user/login?username={login}&password={pwd}'
    response_login = requests.get(url, headers=data.HEADERS_MINI)
    assert response_login.status_code == 400

def test_login_incorrect_username(create_user):
    login = "bad_username"
    pwd = data.body_user['password']
    url = f'{data.BASE_URL}/user/login?username={login}&password={pwd}'
    response_login = requests.get(url, headers=data.HEADERS_MINI)
    assert response_login.status_code == 400

def test_login_not_allowed_method_post():
    url = f'{data.BASE_URL}/user/login?username=login&password=passwd'
    response_login = requests.post(url, headers=data.HEADERS_MINI)
    assert response_login.status_code == 405

def test_login_not_allowed_method_put():
    url = f'{data.BASE_URL}/user/login?username=login&password=passwd'
    response_login = requests.put(url, headers=data.HEADERS_MINI)
    assert response_login.status_code == 405

def test_login_not_allowed_method_delete():
    url = f'{data.BASE_URL}/user/login?username=login&password=passwd'
    response_login = requests.delete(url, headers=data.HEADERS_MINI)
    assert response_login.status_code == 405

def test_logout_incorrect_url():
    url = f'{data.BASE_URL}/usair/logout'
    response_logout = requests.get(url, headers=data.HEADERS_MINI)
    assert response_logout.status_code == 404

def test_logout_not_allowed_method_post():
    url = f'{data.BASE_URL}/user/logout'
    response_logout = requests.post(url, headers=data.HEADERS_MINI)
    assert response_logout.status_code == 405

def test_logout_not_allowed_method_put():
    url = f'{data.BASE_URL}/user/logout'
    response_logout = requests.put(url, headers=data.HEADERS_MINI)
    assert response_logout.status_code == 405

def test_logout_not_allowed_method_delete():
    url = f'{data.BASE_URL}/user/logout'
    response_logout = requests.delete(url, headers=data.HEADERS_MINI)
    assert response_logout.status_code == 405