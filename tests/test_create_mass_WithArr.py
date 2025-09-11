import requests

BASE_URL = 'https://petstore.swagger.io/v2'
HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

data_body_List_0 = [
    {
        "id": 0, "username": "MassCreateUserA", "firstName": "MyName", "lastName": "Familia",
        "email": "example@ex.com", "password": "PASSWORD", "phone": "123456789", "userStatus": 0
    },
]
data_body_List_1 = [
    {
        "id": 0, "username": "MassCreateUserAA", "firstName": "SurName", "lastName": "SecondName",
        "email": "example@ex.com", "password": "PWD1234", "phone": "987654321", "userStatus": 0
    },
    {
        "id": 0, "username": "MassCreateUserAB", "firstName": "", "lastName": "UniqName",
        "email": "example@ex.com", "password": "PAROL", "phone": "192837456", "userStatus": 0
    },
    {
        "id": 0, "username": "MassCreateUserAC", "firstName": "MyName", "lastName": "NoName",
        "email": "example@ex.com", "password": "parol", "phone": "56748392", "userStatus": 0
    }
]

def test_mass_create_1():
    url = f'{BASE_URL}/user/createWithArray'
    response_create = requests.post(url, headers = HEADERS, json = data_body_List_0)
    assert response_create.status_code == 200

def test_mass_create_2():
    url = f'{BASE_URL}/user/createWithArray'
    response_create = requests.post(url, headers = HEADERS, json = data_body_List_1)
    assert response_create.status_code == 200