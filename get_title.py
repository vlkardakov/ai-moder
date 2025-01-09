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

            pre_compare = f"{title}; {h1_tags}; {h2_tags}; {h3_tags};".replace("[","").replace("]","")


            return pre_compare
    except aiohttp.ClientError as e:
        #print(f"({url}): {e}")
        return None, [], [], []
    except AttributeError:
        #print(f"({url}).")
        return None, [], [], []

async def get_page_titles(url):
    async with aiohttp.ClientSession() as session:
        task = get_page_headers(session, url)
        title = await asyncio.gather(task)
        return title

def get_title(url):
    return asyncio.run(get_page_titles(url))#[0]

if __name__ == "__main__":
    while True:
        t = input()

        print(get_title(t))