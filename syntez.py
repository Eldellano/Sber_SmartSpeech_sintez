import requests
import sounddevice as sd
import soundfile as sf
from token_from_api import tocken_get


text_for_sintez = 'Привет Влад! Это тестовый тест чтобы тестировать тесты!'
token = tocken_get()
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/text'}
resp = requests.post("https://smartspeech.sber.ru/rest/v1/text:synthesize",
                     headers=headers,
                     data=text_for_sintez.encode('utf-8'),
                     params={'format': 'wav16',
                             'voice': 'Bys_24000'})
SAMPLE_RATE = 24000


print(resp.status_code)
print(resp.headers)
# print(resp.content)

# Воспроизведение
with open('result.wav', 'wb') as outfile:  # пишем битовый звук в файл
    outfile.write(resp.content)
data, fs = sf.read('result.wav')  # воспроизводим
sd.play(data, fs)
sd.wait()
