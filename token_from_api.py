import requests
import json
import time
import datetime
import username_pass


"""
Получаем последовательно 3 токена от sbercloud via: https://console.sbercloud.ru/smartspeech/aba36afb-6f53-4de8-9e37-e31da06094b9
Парсим последний ответ в tocken_get(), проверяем время жизни токена, при истечении запрашиваем новый. 
При отсутствии файла с токеном создаем его.
"""

KC_USER = username_pass.USER  # получаем userdata из файла
KC_PASSWORD = username_pass.PASSWORD


def get_refresh_token():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    resp = requests.post("https://auth.sbercloud.ru/auth/realms/CP/protocol/openid-connect/token",
                         headers=headers,
                         data={'client_id': 'public-cli',
                               'grant_type': 'password',
                               'username': f'{KC_USER}',
                               'password': f'{KC_PASSWORD}',
                               'scope': 'openid offline_access'})

    js_get = json.loads(resp.content)
    return js_get['refresh_token']


def get_access_token():
    refresh_token = get_refresh_token()
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    resp_access = requests.post("https://auth.sbercloud.ru/auth/realms/CP/protocol/openid-connect/token",
                                headers=headers,
                                data={'client_id': 'public-cli',
                                      'grant_type': 'refresh_token',
                                      'refresh_token': f'{refresh_token}'})

    js_get = json.loads(resp_access.content)
    return js_get['access_token']


def get_smartspeech_tocken():
    smartsppech_token = get_access_token()
    headers = {'Authorization': f'Bearer {smartsppech_token}',
               'Content-Type': 'Content-Type: application/json',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
    resp_smartsppech = requests.get(
        "https://console.sbercloud.ru/api/smartspeech/auth/?service_instance=aba36afb-6f53-4de8-9e37-e31da06094b9",
        headers=headers)

    with open('smartspeech.token', 'wb') as file:  # пишем контент в файл
        file.write(resp_smartsppech.content)


def tocken_get():
    try:
        with open('smartspeech.token', 'rb') as file:
            file_cont = file.read()
        js_get = json.loads(file_cont)
        token = js_get['token']
        exp = js_get['expired_at']
    except FileNotFoundError:  # если файл с токеном не найден
        get_smartspeech_tocken()
        return tocken_get()

    # вычисляем время жизни токена epoch --> human
    date_now = time.localtime(time.time())
    date_token = time.localtime(exp)  # token lifetime
    delta_now = datetime.timedelta(days=date_now.tm_yday, minutes=date_now.tm_min, hours=date_now.tm_hour)
    delta_token = datetime.timedelta(days=date_token.tm_yday, minutes=date_token.tm_min, hours=date_token.tm_hour)
    seconds_left = int((delta_token - delta_now).total_seconds())  # остаток жизни токена в секундах

    # проверка времени жизни токена, новый токен живет 12 часов - 43200 секунд
    if seconds_left < 120:  # секунд
        get_smartspeech_tocken()
        return tocken_get()
    else:
        return token
