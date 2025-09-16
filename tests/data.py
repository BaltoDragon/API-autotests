BASE_URL = 'https://petstore.swagger.io/v2'

#Заголовки
HEADERS_BASE = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

HEADERS_MINI = {
    'accept': 'application/json',
}

#Тестовые данные
body_empty_list = []

body_user_mini = {
    "id": 0, "username": "TestGetUserBD", "password": "PASSWORD"
}

body_user = {
    "id": 0, "username": "nicknameUser", "firstName": "MyName", "lastName": "MyLastName",
    "email": "nicknameUser@ex.com", "password": "PASSWORD", "phone": "1234567890", "userStatus": 0
}

body_user_list = [{
        "id": 0, "username": "nicknameUserList", "firstName": "MyName", "lastName": "MyLastName",
        "email": "nicknameUserList@ex.com", "password": "PASSWORD", "phone": "1234567890", "userStatus": 0
    }
]

body_users_list = [
         {
            "id": 0, "username": "string", "firstName": "string", "lastName": "string",
            "email": "string", "password": "string", "phone": "string", "userStatus": 0
         },
         {
             "id": 0, "username": "nickname", "firstName": "MyName", "lastName": "MyLastName",
             "email": "nickname@ex.com", "password": "PASSWORD", "phone": "1234567890", "userStatus": 0
         },
         {
             "id": 0, "username": "nickname", "firstName": "MyName",
             "email": "example@ex.com", "password": "PASSWORD"
         },
         {
             "id": 0, "username": "a", "firstName": "b", "lastName": "c",
             "email": "d@e.f", "password": "G", "phone": "12", "userStatus": 0
         },
         {
             "id": 0, "username": "n" * 256, "firstName": "f" * 256, "lastName": "l" * 256,
             "email": "e" * 245 + "@ex.com", "password": "p" * 256, "phone": "1" * 256, "userStatus": 1
         }
        ]

body_users_list_incorrect = [
         {
            "id": "string", "username": "string", "firstName": "string", "lastName": "string",
            "email": "string", "password": "string", "phone": "string", "userStatus": 0
         },
         {
             "id": 0, "username": 54234, "firstName": "MyName", "lastName": "MyLastName",
             "email": "nickname@ex.com", "password": "PASSWORD", "phone": "1234567890", "userStatus": 0
         },
         {
             "id": None, "username": "nickname", "firstName": "MyName",
             "email": "example@ex.com", "password": "PASSWORD"
         },
         {
             "id": 0, "username": None, "firstName": "b", "lastName": "c",
             "email": "d@e.f", "password": "G", "phone": "12", "userStatus": 0
         },
        ]

update_data_single = {"email": "example@ex.com"}

update_data_multi = {"lastName": "MyLastName", "phone": "1234567890", "userStatus": 35}

update_data_array = [update_data_single, update_data_multi]