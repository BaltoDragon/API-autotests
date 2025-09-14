BASE_URL = 'https://petstore.swagger.io/v2'

#Заголовки
HEADERS_BASE = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

#Тестовые данные
body_empty_list = []

body_user = {
             "id": 0, "username": "nicknameUser", "firstName": "MyName", "lastName": "MyLastName",
             "email": "example@ex.com", "password": "PASSWORD", "phone": "1234567890", "userStatus": 0
         }

body_user_list = [{
             "id": 0, "username": "nicknameUserList", "firstName": "MyName", "lastName": "MyLastName",
             "email": "example@ex.com", "password": "PASSWORD", "phone": "1234567890", "userStatus": 0
         }
    ]

body_users_list = [
        #0_default_data
         {
            "id": 0, "username": "string", "firstName": "string", "lastName": "string",
            "email": "string", "password": "string", "phone": "string", "userStatus": 0
         },
        #1_real_data
         {
             "id": 0, "username": "nickname", "firstName": "MyName", "lastName": "MyLastName",
             "email": "example@ex.com", "password": "PASSWORD", "phone": "1234567890", "userStatus": 0
         },
        #2_mini_data
         {
             "id": 0, "username": "nickname", "firstName": "MyName",
             "email": "example@ex.com", "password": "PASSWORD"
         },
        #3_short_string
         {
             "id": 0, "username": "a", "firstName": "b", "lastName": "c",
             "email": "d@e.f", "password": "G", "phone": "12", "userStatus": 0
         },
        #4_long_string
         {
             "id": 0, "username": "n" * 256, "firstName": "f" * 256, "lastName": "l" * 256,
             "email": "e" * 245 + "@ex.com", "password": "p" * 256, "phone": "1" * 256, "userStatus": 1
         }
        ]