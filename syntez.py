import requests
import sounddevice as sd
import soundfile as sf


text_for_sintez = 'Привет Влад! Это тестовый тест чтобы тестировать тесты!'
token = 'eyJhbGciOiJSU0EtT0FFUC0yNTYiLCJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwidHlwIjoiU0MifQ.nqpwNTWs9K0EQWMFSDvfmXLjam_DNzDIwiY1xZzXaemuFmz3s3w9IDCTmBII8s0O660Z_N8LzF5Uc1TwrPnjH0Ftz2O_xhPu_KxYBflKTjhV8YbjrlZPdD4JAKc0XvCjT_RjNLQhoDL8UWITEY_TIaqzSDDryi6bgSXH7ZCHKi7jrDxGGtEVCOuT2E0_2jtUB_Zf2Hi8aXT_9QlHtq5N0vY5H58huQv18XgfgUHn5pnyaRW0baKjxPgWwJ_KuAbphK0rXVBF_SQn5kRCzRjqBXQZNn8amzSMjJM5sEI4FZgtZ8ae6gTImpmY5noazznTDSPm8D4FFvGoKs-WMDiKmw.dXdgVU5djNIKpMtTZuzUIQ.haORldZlFp3PI9y0F1VhaqewVjltSEWFKo7ptj2-gZ31QHC-KkW-YsEnjuNlyVzrw2tVXiRbdlv12PdTAh_klmM14OmULvG8ZqKV9nDvwxKjahO1pqiITPP0Es_eh9JK6TXlk0LAqxLK8DZ9Fqjag2wX8yvdTrFp-lKRagY0_LpWWqJed8Nn2gb5kBnlYVoA23oYZOl__8Aomb1G-MHn-w2vhF1oO_OvwLSijkofMBdUCmdgBDyxFipL1fbea6Akgme-ggEF2a5dZ9izQ9BiQKJw-sl-7qeAWjGRqYnPZgPfthBNNrl7DNK7ub1LoxwYConeQ6eNvzxMKZkW7Mm3eRLpuCLwvg5BjBtX5BlUEReUD7ZfMrldKmNvcb-Opt3_jU7TdwLS5hxGTDTeHnzLZ36GJOdv6IXbpZKjMfsInT9ARmZE4dJnt58pzjqcpCE50KJwym4JOD3HomiJHYlSTir9u_4E4dmvz4cM1K7M76wyuHI-IY3jLlmt2vEKNyXnO3ZnLSDNTKJWaCf7uaDF82RjDzrsDExynTY2Y5rKlGny3iw1-03dI_DaddNhMe6Ey6KeuW8Osfql6vz_WAi6v1wfPETbGor3tpBc_6oAq16Y9SVAJSEurytWajCrHrMt1E_2UFV37rUOuFGueDJVm6Xg6wrp7_AeF324KyXC5J02zyYo4Oejjg7l1TN61pOZL4Nv-s688WFUT_4w_-Ke7-kiScJc7X2iWzse9YuJZsV84PbKP9FNoVaPYI183arZO-qRllLTBn1EP52rHnE49C0J1yR92FDjgqKCFMbE_ccrZbr__rU5iCRjuIOFFDUqj_YYrc9DJzA3m6oFHlRrKHBESv6NRusWL-aFyF4m2b9EMnS2Jiu65J5vEAO9EY58zfAYh3-zzhBQYRqG__2WRDmLzARSr2if4QM_mpVWjeE-icqMFrNlImc12wit8LJrveV6q8sO-6N0WhYgncnBXKorlBCVeNSa8Y6y_pNl7nrsxmZt2U_r5WsQxnsK83fDZLhpuj5n89cgfhjETDkdr-hd13ryrZkmbAvWHQuSyImIxgwIv5U0JWeUifvuupzbT4jNU3nO4Db6D9Cr-QWpsZvwilFC2-r56FL-ncbC3sWaspPLkwgK9L5qdJOMNJtpdZ5f2FtPTHyyovHLSW5A3w.whT1o3kviMVqX8W26vryKeGjMto4ZKE7EK9bvSVBY7g'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/text'}
resp = requests.post("https://smartspeech.sber.ru/rest/v1/text:synthesize",
                     headers=headers,
                     data=text_for_sintez.encode('utf-8'),
                     params={'format': 'wav16',
                             'voice': 'Bys_24000'})
SAMPLE_RATE = 24000


# print(resp.status_code)
# print(resp.headers)
# print(resp.content)

# Воспроизведение
with open('result.wav', 'wb') as outfile:  # пишем битовый звук в файл
    outfile.write(resp.content)
data, fs = sf.read('result.wav')  # воспроизводим
sd.play(data, fs)
sd.wait()
