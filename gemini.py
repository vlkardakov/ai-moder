import os
import google.generativeai as genai
import os
import numpy as np
import time

api_keys = [
    "AIzaSyAPL9cKR86Aj5nqXsIvD_YWDUZ7E8vEyec", # работает
    "AIzaSyBVpBV7gnTa_XVoCFOcBY4oWRzY0hmGwXQ", # работает
    #"AIzaSyArqyXBQrwXLYg26slozZG1BLnHfRpDEM4",
    #"AIzaSyDj1cDXsTKkC7mMroHhIgg37X6MtqgjUmw",
    "AIzaSyCF4gSrVqI7wqP8jfOdD7V-fDo_TAImflY", # 9
    "AIzaSyDENOL9VDuCYYKsx_GkaYa_7qjrSPgiONM", # 10
    "AIzaSyCfLsRDmgJcgbkVVFGXOzIOd4heFtsvnnM", # mail@vlkardakov.ru
    "AIzaSyBX2ERx5-x6tnctQgED7MK5YWBXHFkeQJ0", # 11
    "AIzaSyA4BJ03mlU-hff2wqOH2Gh_YsqMMhcF1NE", #АБОБА
    # "","","","","","","","",""
]

key_index = 0
current_key = api_keys[0]


def get_next_api_key():
    global key_index

    key_index = (key_index + 1) % len(api_keys) # Circular increment
    api_key = api_keys[key_index]

    return api_key

def gemini(zapros):
    global key_index, api_keys, zaprosi_history, current_key

    for i in range(len(zaprosi_history) - 1, -1, -1):
        if zaprosi_history[i]["time"] - time.time() < 60:
            break
        else:
            del zaprosi_history[i]

    current_key = get_next_api_key()

    genai.configure(api_key=current_key)

    model = genai.GenerativeModel('gemini-1.5-fl')

    response = model.generate_content([], stream=True)
    response.resolve()

    result = response.text
    if isinstance(result, bytes):
        result = result.decode('utf-8', errors='replace')

    return result