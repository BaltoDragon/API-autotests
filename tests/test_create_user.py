import data
import pytest
import requests

@pytest.mark.parametrize('testing_data', data.body_users_list)
def test_create_0(testing_data):
    url = f'{data.BASE_URL}/user'
    response_create = requests.post(url, headers = data.HEADERS_CREATE, json = testing_data)
    assert response_create.status_code == 200

def test_create_1():
    url = f'{data.BASE_URL}/user'
    response_create = requests.post(url, headers = data.HEADERS_CREATE, json = data.body_users_list)
    assert response_create.status_code == 400