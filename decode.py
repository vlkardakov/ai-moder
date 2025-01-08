import requests
from urllib.parse import urlparse, parse_qs, unquote
from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.error import HTTPError, URLError

def load_params():
    with open("params.txt", "r") as f:
        return pithon(f"result = {f.read()}")

def pithon(code):
    global result
    try:
        local_vars = {}
        exec(code, {}, local_vars)  # Используем локальный словарь для хранения переменных
        return local_vars.get('result')  # Возвращаем значение переменной result
    except Exception as e:
        return e


def final_from_url(latest):
    params = ["redirect",'redir','r',
              'link',
              'go_to','goto','go',
              'returnUrl','aurl','url','u','p','q'
              'target','targ','get']
    for i in range(10):
        for el in params:
            latest = decode(latest.split(f"?{el}=")[-1])

        for el in params:
            latest = decode(latest.split(f"&{el}=")[-1])

        latest = latest.strip().strip("/")

    return latest

def decode(url):
    return unquote(unquote(unquote(url)))

def redirects(url):
    try:
        url = decode(url)
        response = urlopen(url)
        final_url = response.geturl()
        #print("URL Получен!")
        return decode(final_url)
    except HTTPError as e:
        # Обработка HTTP ошибок (например, 404, 500)
        print(f"HTTP Error: {e.code} for URL: {url}")
        return url  # Возвращаем исходный URL, так как редиректа не было
    except URLError as e:
        # Обработка ошибок URL (например, неправильный формат URL)
        print(f"URL Error: {e.reason} for URL: {url}")
        return url
    except Exception as e:
        # Обработка других возможных ошибок
        print(f"An unexpected error occurred: {e}")
        return url
    except:
        return url



def decode_url(link):
    url = decode(link)

    latest = final_from_url(url) #final_from_redirect(final_from_url(final_from_redirect(final_from_url(url))))
    latest = redirects(latest)
    latest = final_from_url(latest)
    if latest != url:
        print(f"редирект для {url}: {latest}")
        return latest
    else:
        print(f"редирект для {url}: нету редиректа")
        return "noredir"

if __name__ == "__main__":
    url = input("URL = ")
    print(f"\nURL: {decode_url(url)}")