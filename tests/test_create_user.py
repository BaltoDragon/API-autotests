import pytest
import requests

BASE_URL = 'https://petstore.swagger.io/v2'
HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

data_body = [
        #default_data
         {
            "id": 0, "username": "string", "firstName": "string", "lastName": "string",
            "email": "string", "password": "string", "phone": "string", "userStatus": 0
         },
        #real_data
         {
             "id": 0, "username": "nickname", "firstName": "MyName", "lastName": "MyLastName",
             "email": "example@ex.com", "password": "PASSWORD", "phone": "1234567890", "userStatus": 0
         },
        #mini_data
         {
             "id": 0, "username": "nickname", "firstName": "MyName",
             "email": "example@ex.com", "password": "PASSWORD"
         },
        #short_string
         {
             "id": 0, "username": "a", "firstName": "b", "lastName": "c",
             "email": "d@e.f", "password": "G", "phone": "12", "userStatus": 0
         },
        #long_string
         {
             "id": 0, "username": "n" * 256, "firstName": "f" * 256, "lastName": "l" * 256,
             "email": "e" * 245 + "@ex.com", "password": "p" * 256, "phone": "1" * 256, "userStatus": 1
         }
        ]

@pytest.mark.parametrize('testing_data', data_body)
def test_create(testing_data):
    url = f'{BASE_URL}/user'
    response_create = requests.post(url, headers = HEADERS, json = testing_data)
    assert response_create.status_code == 200