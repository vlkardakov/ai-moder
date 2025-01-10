from urllib.parse import urlparse, parse_qs, unquote, urljoin
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from gemini import gemini
import random
#

import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def get_page_headers(session, url):
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=4)) as response:
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
        print(f"Error getting headers for ({url}): {e}")
        return None
    except AttributeError:
        print(f"AttributeError getting headers for ({url}).")
        return None
    except asyncio.TimeoutError:
        print(f"Timeout getting headers for ({url}).")
        return None

async def get_page_titles(session, url):
    title = await get_page_headers(session, url)
    return title

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
    for _ in range(10):
        for el in params:
            if f"?{el}=" in latest:
                latest = decode(latest.split(f"?{el}=")[-1])

        for el in params:
            if f"&{el}=" in latest:
                latest = decode(latest.split(f"&{el}=")[-1])

        latest = latest.strip().strip("/")

    return latest

def decode(url):
    return unquote(unquote(unquote(url)))

async def async_redirects(session, url):
    try:
        i = random.randint(0,100)
        print(f"{i} обработка started")
        url = decode(url)
        async with session.get(url, allow_redirects=True, timeout=aiohttp.ClientTimeout(total=4)) as response:
            final_url = str(response.url)
            print(f"URL получен! для {i}")
            return decode(final_url).strip("/")
    except aiohttp.ClientError as e:
        print(f"Aiohttp Client Error: {e} for URL: {url}")
        return url
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return url
    except asyncio.TimeoutError:
        print(f"Timeout during redirect for URL: {url}")
        return url

async def async_describe_url(session, link):
    before_url = decode(link).strip("/")
    url = before_url

    url = final_from_url(url)
    url = await async_redirects(session, url)
    url = final_from_url(url)
    return before_url, url

async def get_title_async(session, url):
    title_str = await get_page_titles(session, url)
    return title_str

async def process_url(session, url):
    before, after = await async_describe_url(session, url)
    title = await get_title_async(session, after)
    return {"before": before, "after": after, "title": title}

async def describe_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [process_url(session, url.encode("latin-1")) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Example usage:
def describe_url(urls):
    return asyncio.run(describe_urls(urls))

if __name__ == '__main__':
    test_urls = [
        "https://google.com",
        "https://example.com?go_to=https://www.google.com",
        "https://www.youtube.com",
        "http://httpbin.org/delay/5" # Example of a slow loading page
    ]

    results = describe_url(test_urls)
    for result in results:
        print(result)