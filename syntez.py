import requests
import sounddevice as sd
import soundfile as sf


text_for_sintez = 'Привет Влад! Это тестовый тест чтобы тестировать тесты!'
token = 'eyJhbGciOiJSU0EtT0FFUC0yNTYiLCJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwidHlwIjoiU0MifQ.nQmPV86lYeNFeFcXAMx-tr3-YcVW2Y5OqV1K3POx2vpOzPJP-9KTp6PXnOjw6XBqJVFmCQvKZwvL6jpqitEEhB3gMMZCSOXqD6REw0PQMxLvSzj-KqlFDRYCWN6XqCKEqW-ZJ9mAPBBoaocstnEmB_y8FpLvOumHT7VPwLrVvuExpFaOm3ZiqQ5cHrLTtYR1XIlMnVQVG0HAP5DdXY5BUqDXhw_HJRIzu8_-5-69zWqwmTd8-ZABjEA6pYxttYCkSxH3dtZQTdQNs65pZ1LMAn6RKIlZjcY8__l7ukD1JgKOVjjeroZJiejck-gdwtBAWDK_cWXUKHRxkFnY9MnkFA.81qRSRGId8HX7u6ZJrXxBg.IrIvWNMwmPOjbX-KRFhH1ERcD9qdCTUe-2pzuoJBvttKJFwpxtGGCzNo3GtA6FpaQTR4YftgqL5xHzp7rUk0G9Zhi2qc3G8QgzIvPD0F0IXoHTuwlVnqlkzeVhgxqPPxMQoDR8Kx-1N8uRJ6YJFQmOCEqd-9GZkjGMlWiWCdM0Mno6dt-3COOrxYHLYodbPMOTczq0phcITIcLlI10zD3syI_XeODdBW_6HpLAKdhaB0eTSt5DSV5DPqRzV9FMf4c_fHW1rSnNe8eaiy94sVGxvwNDwUynpNrWlqSt2Q2tx5mj5MmVg24i9TeIpRK0fERrl-fOnGjwUwx4Awq4erXHyB5CajUxabyMazuu2QkftODF4ePC24cq-FusxMt3N-2ZUHmQ8gQ_xUIWh14mgAsB-_WjslbpVxKx1Fae_yqvcZdl_K9I8qEjSjgNAKg7V91MAz23ag8OzjsNmKgUPbvQKg2iRcXVI2h-9jb-pO49H3aYjjC_UrKqSeQhzYDHZa549zx_hoOCsOkYP7z0mR4hVtL9kYse6ODBs4t1ymstiKFsOTZIbEk_u0lcSYfdsJZbZyF0WGnAUGbet9nKY6TR5eWVI3isqk5sBNqU9DfV8ou78zLBRWC0FBRPG82XOYJUpOdGckTqQxHDNcc-HQ3gjcr1sCgj_jaqu19pi007G-IHknevfFKhEA4o6nAtZEZKglL0lYcidVooC60huqYoLQOpIL-Oe6KtMMpIoIf13KqxUIECHyouoZNdBcaWz2__IuGh8GiV7-gXgpaDCaX7lMlNyD0gxBdKJvtFdIehdqkEYyAtiNp6tkTRngCVPvQ-iF1LaO15lVRH_NOw20boSKe6kW_JRxE7n5vfalNH34W3tuvUTlh0uYW6XQYg1-FEPtSiE_ClJVm7gnoayfN6jQYphGvEmJt4UH92-MfZCryffZDuV2pyzVygRVHAvboZHsO8gHJxbdibaJ6R5PYIpSoeISwj4To2KZbNpfcm0XBxW7DxuRV5_4esu6K9fUG3dzHY1VSauxDfviQ3dkRyPcg-TffvK5V8SiTjYzCb_6vOG2pSnQH8J6LXgOfCy982qPgCPipiaKXw6GGVyhP2bNIrWFQIVZODUktjFgl_65spZKCVhmhaWgkBFfuS4SzTVMeTpwe2p0q1u_fhmeYnrrj6w9z1TjuNmHbQXWp2FLe6ViAErlaCQ2BBHwRDBziKGZvc9e1TqXTHieuIn54g.m1bR45uLVTF3NXPlJdgFhqYgXfq_6NngqO_rd0CXu1M'
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
