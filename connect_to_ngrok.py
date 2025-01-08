import requests
from random import randint


def decode(text):
    url = f"http://83.143.112.43:444{randint(0,9)}"
    data = {'url': text}
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        #print("УСПЕШНО.")
        #print("ОТВЕТ:", response.text, "\n")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"ОШИБКА ЗАПРОСА: {e}")
        return text


while True:
    text = input("ЧТО ОТПРАВИТЬ: ")
    print(decode(text))