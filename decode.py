from urllib.parse import urlparse, parse_qs, unquote, urljoin
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from gemini import gemini
#

import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def get_page_headers(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')

            title_tag = soup.title
            title = title_tag.string.strip() if title_tag and title_tag.string else None

            h1_tags = [tag.string.strip() for tag in soup.find_all('h1') if tag.string]
            h2_tags = [tag.string.strip() for tag in soup.find_all('h2') if tag.string]
            h3_tags = [tag.string.strip() for tag in soup.find_all('h3') if tag.string]

            pre_compare = f"{title}; {h1_tags}; {h2_tags}; {h3_tags};".replace("[", "").replace("]", "")

            return pre_compare
    except aiohttp.ClientError as e:
        # print(f"({url}): {e}")
        return None, [], [], []
    except AttributeError:
        # print(f"({url}).")
        return None, [], [], []


async def get_page_titles(url):
    async with aiohttp.ClientSession() as session:
        task = get_page_headers(session, url)
        title = await asyncio.gather(task)
        return title


def get_title(url):
    return asyncio.run(get_page_titles(url))[0]


def load_params():
    with open("params.txt", "r") as f:
        return pithon(f"result = {f.read()}")


def pithon(code):
    global result
    try:
        local_vars = {}
        exec(code, {}, local_vars)
        return local_vars.get('result')
    except Exception as e:
        return e


def final_from_url(latest):
    params = load_params()
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
        print("URL получен!")
        return decode(final_url).strip("/")
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


def describe_url(link):
    url2 = decode(link).strip("/")
    url = url2

    url = final_from_url(url)
    url = redirects(url)
    url = final_from_url(url)
    return url