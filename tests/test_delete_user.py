import pytest
import requests
import time

BASE_URL = 'https://petstore.swagger.io/v2'
HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

@pytest.fixture()
def create_user():
    data_body = {
        "id": 0, "username": "UniqUserNewID", "firstName": "MyName",
        "email": "example@ex.com", "password": "PASSWORD"
    }
    url = f'{BASE_URL}/user'
    request = requests.post(url, headers=HEADERS, json=data_body)
    print(request.json())
    time.sleep(10)
    username = data_body['username']
    url = f'{BASE_URL}/user/{username}'
    userdata = requests.get(url, headers=HEADERS)
    print(userdata.json())
    return userdata.json()

def test_delete_code_200(create_user):
    url = f'{BASE_URL}/user/{create_user['username']}'
    response_delete = requests.delete(url)
    assert response_delete.status_code == 200