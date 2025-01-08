from flask import Flask, request, jsonify, Response
import requests
from urllib.parse import urlparse, parse_qs, unquote, urljoin
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

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
        print("URL Получен!")
        return decode(final_url)
    except HTTPError as e:
        print(f"HTTP Error: {e.code} for URL: {url}")
        return url
    except URLError as e:
        print(f"URL Error: {e.reason} for URL: {url}")
        return url
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return url
    except:
        return url


def decode_url(link):
    url = decode(link)

    latest = final_from_url(url) #final_from_redirect(final_from_url(final_from_redirect(final_from_url(url))))
    latest = redirects(latest)
    latest = final_from_url(latest)
    return latest


app = Flask(__name__)

@app.route("/", methods=["POST"])
def givedata():
    url = request.form.get('url', '')
    return decode_url(url)

if __name__ == '__main__':
    print("СЕРВЕР НАЧАЛСЯ")
    app.run(debug=True, host='0.0.0.0', port=4444)