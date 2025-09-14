import data
import pytest
import requests

@pytest.mark.parametrize('testing_data', data.body_users_list)
def test_create_delete_single_user(testing_data):
    url = f'{data.BASE_URL}/user'
    response_create = requests.post(url, headers = data.HEADERS_BASE, json = testing_data)
    assert response_create.status_code == 200

    username = testing_data['username']
    url = f'{data.BASE_URL}/user/{username}'
    response_delete = requests.delete(url)
    assert response_delete.status_code == 200

def test_create_single_user_with_array():
    url = f'{data.BASE_URL}/user'
    response_create = requests.post(url, headers = data.HEADERS_BASE, json = data.body_users_list)
    assert response_create.status_code == 400

def test_create_incorrect_url():
    url = f'{data.BASE_URL}/usair'
    response_create = requests.post(url, headers = data.HEADERS_BASE, json = data.body_user)
    assert response_create.status_code == 404

def test_create_not_allowed_method_get():
    url = f'{data.BASE_URL}/user'
    response_create = requests.get(url, headers = data.HEADERS_BASE, json = data.body_user)
    assert response_create.status_code == 405

def test_create_not_allowed_method_put():
    url = f'{data.BASE_URL}/user'
    response_create = requests.put(url, headers = data.HEADERS_BASE, json = data.body_user)
    assert response_create.status_code == 405

def test_create_not_allowed_method_delete():
    url = f'{data.BASE_URL}/user'
    response_create = requests.delete(url, headers = data.HEADERS_BASE, json = data.body_user)
    assert response_create.status_code == 405