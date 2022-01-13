import requests
import json
import username_pass

#TODO: проверка времени жизни токена, запрос нового при истечении
KC_USER = username_pass.USER
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
    # print(resp_access.status_code)
    # print(resp_access.headers)
    # print(resp_access.content)
    js_get = json.loads(resp_access.content)
    return  js_get['access_token']

def get_smartspeech_tocken():
    smartsppech_token = get_access_token()
    headers = {'Authorization': f'Bearer {smartsppech_token}',
               'Content-Type': 'Content-Type: application/json',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
    resp_smartsppech = requests.get("https://console.sbercloud.ru/api/smartspeech/auth/?service_instance=aba36afb-6f53-4de8-9e37-e31da06094b9",
                         headers=headers)#,
                         # data={'client_id': 'public-cli',
                         #       'grant_type': 'refresh_token',
                         #       'refresh_token': f'{smartsppech_token}'})
    # print(resp_smartsppech.status_code)
    # print(resp_smartsppech.headers)
    print(resp_smartsppech.content)
    js_get = json.loads(resp_smartsppech.content)
    print(js_get['token'])


# print(resp.status_code)
# print(resp.headers)
# print(resp.content)

get_smartspeech_tocken()
