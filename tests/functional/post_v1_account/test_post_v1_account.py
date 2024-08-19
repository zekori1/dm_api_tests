import requests

def test_post_v1_account():
    # Регистрация пользователя

    login = 'ivan_kochetkov_3'
    password = 'ivan_kochetkov_123'
    email = f'{login}@mail.ru'

    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = requests.post('http://5.63.153.31:5051/v1/account', json=json_data)

    print(response.status_code)
    print(response.text)

    # Получить письма из почтового сервера

    url = "http://5.63.153.31:5025/api/v2/messages?limit=50"

    payload = {}

    response = requests.get(url, data=payload)

    print(response.status_code)
    print(response.text)

    # Получить активационный токен

    ...

    # Активация токена

    headers = {
        'accept': 'text/plain',
    }

    response = requests.put('http://5.63.153.31:5051/v1/account/34ade58a-3ee6-4143-b7a0-763d2d4ba860', headers=headers)

    print(response.status_code)
    print(response.text)

    # Авторизоваться

    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = requests.post('http://5.63.153.31:5051/v1/account/login', json=json_data)

    print(response.status_code)
    print(response.text)
