import data
import requests
import pytest

@pytest.mark.parametrize('user_array', [data.body_empty_list, data.body_user_list, data.body_users_list])
def test_mass_create_0(user_array):
    url = f'{data.BASE_URL}/user/createWithArray'
    response_create = requests.post(url, headers = data.HEADERS_CREATE, json = user_array)
    assert response_create.status_code == 200

def test_mass_create_1():
    url = f'{data.BASE_URL}/user/createWithArray'
    response_create = requests.post(url, headers = data.HEADERS_CREATE, json = data.body_users_list[1])
    assert response_create.status_code == 400