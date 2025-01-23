from urllib.parse import urlparse, parse_qs, unquote, urljoin
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from gemini import gemini
import random
import requests
from bs4 import BeautifulSoup

def get_page_headers(url):
    try:
        response = requests.get(url, timeout=4)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        title_tag = soup.title
        title = title_tag.string.strip() if title_tag and title_tag.string else None

        h1_tags = [tag.string.strip() for tag in soup.find_all('h1') if tag.string]
        h2_tags = [tag.string.strip() for tag in soup.find_all('h2') if tag.string]
        h3_tags = [tag.string.strip() for tag in soup.find_all('h3') if tag.string]

        pre_compare = f"{title}; {h1_tags}; {h2_tags}; {h3_tags};".replace("[", "").replace("]", "")

        return pre_compare
    except requests.exceptions.RequestException as e:
        print(f"Error getting headers for ({url}): {e}")
        return None
    except AttributeError:
        print(f"AttributeError getting headers for ({url}).")
        return None
    except requests.exceptions.Timeout:
        print(f"Timeout getting headers for ({url}).")
        return None

def get_page_titles(url):
    title = get_page_headers(url)
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
    for i in range(2):
        for el in params:
            try:
                pre_latest = decode(latest.split(f"?{el}=")[-1])
                if "." in pre_latest or "http" in pre_latest:
                    latest = pre_latest
            except IndexError:
                pass  # Handle cases where the parameter is not found

        for el in params:
            try:
                pre_latest = decode(latest.split(f"&{el}=")[-1])
                if "." in pre_latest or "http" in pre_latest:
                    latest = pre_latest
            except IndexError:
                pass  # Handle cases where the parameter is not found

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
    except:
        return url

def final_link(link):
    url = decode(link).strip("/")


    url = final_from_url(url)
    #url = redirects(url)
    #url = final_from_url(url)

    return url

thread_index = 0

def sync_redirects(url):
    global thread_index
    thread_index += 1
    try:
        print(f"{thread_index} обработка started")
        url = decode(url)
        response = requests.get(url, allow_redirects=True, timeout=2)
        final_url = str(response.url)
        print(f"URL получен! для {thread_index}")
        return decode(final_url).strip("/")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка для {thread_index}: Requests Error: {e} for URL: {url}")
        return url
    except Exception as e:
        print(f"Ошибка для {thread_index}: An unexpected error occurred: {e}")
        return url
    except requests.exceptions.Timeout:
        print(f"Ошибка для {thread_index}: Timeout during redirect for URL: {url}")
        return url

def get_before_and_after(link):
    before_url = decode(link).strip("/")
    url = before_url

    url = final_link(url).strip("/")
    return before_url, url

def get_title_sync(url):
    title_str = get_page_titles(url)
    return title_str

def process_url(url):
    before, after = get_before_and_after(url)
    title = get_title_sync(after)
    return {"before": before, "after": after, "title": title}

def describe_url(urls):
    results = []
    for url in urls:
            print(f"{url=}")
            #try:
            results.append(process_url(url))
            #except Exception as e:
            #print(f"Error processing URL {url}: {e}")
            #pass
    return results

# Example usage:
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