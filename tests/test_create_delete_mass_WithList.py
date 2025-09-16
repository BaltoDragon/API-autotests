import data
import requests
import pytest

@pytest.mark.parametrize('user_list', [data.body_empty_list, data.body_user_list, data.body_users_list])
def test_mass_list_create_delete_users(user_list):
    url = f'{data.BASE_URL}/user/createWithList'
    response_create = requests.post(url, headers = data.HEADERS_BASE, json = user_list)
    assert response_create.status_code == 200

    count = len(user_list)

    if count != 0:
        for i in range(count):
            user = user_list[i]
            username = user['username']
            url = f'{data.BASE_URL}/user/{username}'
            response_delete = requests.delete(url)
            assert response_delete.status_code == 200

def test_mass_list_create_single_user():
    url = f'{data.BASE_URL}/user/createWithList'
    response_create = requests.post(url, headers = data.HEADERS_BASE, json = data.body_users_list[1])
    assert response_create.status_code == 400

def test_mass_list_create_incorrect_url():
    url = f'{data.BASE_URL}/usedr/createWithList'
    response_create = requests.post(url, headers = data.HEADERS_BASE, json = data.body_user_list)
    assert response_create.status_code == 404

def test_mass_array_create_incorrect_data():
    url = f'{data.BASE_URL}/user/createWithList'
    response_create = requests.post(url, headers = data.HEADERS_BASE, json = data.body_users_list_incorrect)
    assert response_create.status_code == 405

def test_mass_list_create_not_allowed_method_get():
    url = f'{data.BASE_URL}/user/createWithList'
    response_create = requests.get(url, headers = data.HEADERS_BASE, json = data.body_user_list)
    assert response_create.status_code == 405

def test_mass_list_create_not_allowed_method_put():
    url = f'{data.BASE_URL}/user/createWithList'
    response_create = requests.put(url, headers = data.HEADERS_BASE, json = data.body_user_list)
    assert response_create.status_code == 405

def test_mass_list_create_not_allowed_method_delete():
    url = f'{data.BASE_URL}/user/createWithList'
    response_create = requests.delete(url, headers = data.HEADERS_BASE, json = data.body_user_list)
    assert response_create.status_code == 405