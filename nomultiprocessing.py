from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from urllib.parse import urlparse
import os


def get_domain(url):
    return urlparse(url).netloc


def normal_filename(link):
    return "screenshots/" + link.replace("https://", "").replace("http://", "").replace("/", "_").replace(":",
                                                                                                          "_").replace(
        "?", '').replace('=', '').replace('%', '') + ".png"


def process_link(link):
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--headless")
    options.add_argument("--start-maximized")

    driver = webdriver.Firefox(options=options)

    output = normal_filename(link)
    if os.path.exists(output):
        os.remove(output)

    driver.get(link)
    title = driver.title
    driver.save_screenshot(output)
    driver.quit()

    print(f"Скриншот сохранен как {output}")

    return {"url": link, "title": title, "screenshot": output, "domain": get_domain(link)}


if __name__ == "__main__":
    links = ["https://google.com", "https://amazon.com", "https://yandex.ru", "https://minilink.pro"]

    data = []
    for link in links:
        data.append(process_link(link))

    for el in data:
        print(el)
