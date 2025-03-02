from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from urllib.parse import urlparse
import os
import tempfile

def get_domain(url):
    return urlparse(url).netloc

def normal_filename(link):
    return "screenshots/" + link.replace("https://", "").replace("http://", "") \
           .replace("/", "_").replace(":", "_").replace("?", "").replace("=", "") \
           .replace("%", "") + ".png"

def process_link(link):
    try:
        print('задаём драйвер')
        options = Options()
        options.add_argument("--log-level=3")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--incognito")

        # Создаем уникальную временную директорию для профиля
        temp_dir = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={temp_dir}")

        # Путь к бинарнику Chromium
        options.binary_location = '/usr/bin/chromium-browser'

        # Путь к драйверу Chromium
        driver_path = '/usr/lib/chromium-browser/chromedriver'
        service = Service(executable_path=driver_path)

        driver = webdriver.Chrome(service=service, options=options)
        print("Драйвыер заадн")
        output = normal_filename(link)
        if os.path.exists(output):
            os.remove(output)

        driver.get(link)
        title = driver.title
        driver.save_screenshot(output)
        driver.quit()

        print(f"Скриншот сохранен как {output}")
        return {"url": link, "title": title, "screenshot": output, "domain": get_domain(link)}
    except Exception as e:
        print(f"Ошибка при обработке {link}: {e}")
        return None

if __name__ == "__main__":
    links = ["https://google.com", "https://amazon.com", "https://yandex.ru", "https://minilink.pro"]
    results = []
    for link in links:

        result = process_link(link)
        results.append(result)
    for res in results:
        print(res)
