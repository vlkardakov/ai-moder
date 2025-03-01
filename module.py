import google.generativeai as genai
import numpy as np
from mss import mss
from PIL import Image
import time
import os

# proxy = 'http://hAnuPVxQqi:DgH2Yc44lq@109.120.129.171:59597'
# os.environ['http_proxy'] = proxy
keys_proxies = [
    {"key":"AIzaSyBm8TubjcNxTtzlZgElnY5ZuCXkADCAQRE", "proxy":'http://vova:2213@193.124.133.94:35068'},#1z`
    {"key":'AIzaSyCpI5SpoP5T44PXGyi-uyHKV-g0N66eNFA', "proxy":'http://vova:2213@193.124.133.151:53136'}, #балбоб
    {"key":'AIzaSyAthBC1Ew0-TTUBnJtpndD44I-7ZWvPhcw', "proxy":'http://vova:2213@193.124.133.184:38562'},#vity 19
    {'key':"AIzaSyCL9WRRrGeCAAfWi-iLEwAkW1DLvepIRcY", "proxy":'http://germ:germ@194.31.73.4:38064'}, #v0681197@gmail.com
    {'key':"AIzaSyA25EIdaG7hmsjF5Ry3GrroW0d0g24Oj5s", "proxy":'http://germ:germ@194.31.73.199:21863'}, # vitya.kardakov19@gmail.com
    {'key':"AIzaSyDW3nj2rrEuJBNNMfybumVxVfZn2_wyOB8", "proxy":'http://germ:germ@194.31.73.93:40032'}, # vikt0r19.kardakov19@gmail.com
    {'key':"AIzaSyBnfHaqOYL3h4eer1bV7nnN7U_KuGQqGkE", "proxy":'http://hAnuPVxQqi:DgH2Yc44lqgerm@109.120.129.171:59597'}, # dcookeiw2@gmail.com
    #'',
    #'',
]



key_index = 0
current_key_proxy = keys_proxies[0]

zaprosi_history = []

def get_next():
    global key_index

    key_index = (key_index + 1) % len(keys_proxies)
    key_proxy = keys_proxies[key_index]

    return key_proxy

def describe(zapros, img):
    global key_index, keys_proxies, zaprosi_history, current_key

    for i in range(len(zaprosi_history) - 1, -1, -1):
        if zaprosi_history[i]["time"] - time.time() < 60:
            break
        else:
            del zaprosi_history[i]

    current = get_next()
    current_proxy = current["proxy"]
    current_key = current["key"]


    zaprosi_history = []
    print(f"ключ {current_key}, прокси {current_proxy}")

    os.environ['http_proxy'] = current_proxy
    # os.environ['HTTP_PROXY'] = current_proxy
    # os.environ['https_proxy'] = current_proxy
    # os.environ['HTTPS_PROXY'] = current_proxy
    genai.configure(api_key=current_key)

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content([
        f"запрос пользователя: {zapros}",
        img
    ], stream=True)
    response.resolve()

    zaprosi_history.append({"time":time.time(), "text":response.text})
    result = response.text
    if isinstance(result, bytes):
        result = result.decode('utf-8', errors='replace')

    return result

if __name__ == "__main__":
    while True:
        with mss() as sct:
            mon = sct.monitors[0]
            chat_config = {
                "top": mon["top"] + 87,  # 100px from the top
                "left": mon["left"] + 374,  # 100px from the left
                "width": mon["width"] - 880,  # 2800,  # Исправлено: width вместо what
                "height": 648
            }
        with mss() as sct:
            sct_img = sct.grab(chat_config)
            img_np = np.frombuffer(sct_img.bgra, dtype=np.uint8).reshape(sct_img.height, sct_img.width, 4)
            img_np = img_np[..., :3][:, :, ::-1]  # BGRA -> RGB
            img = Image.fromarray(img_np)
            img = img.resize((320, 180))  # Resize for comparison
        #t = input("::")
        print(describe("Проанализируй изображение и назови программу, в которой был сделан скриншот. Только название.", img))