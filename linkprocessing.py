from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from urllib.parse import urlparse
import os, time
from concurrent.futures import ThreadPoolExecutor
from get_domain import get_domain
import numpy as np

def save_checked(checked):
    with open("checked_domains.txt", "w") as f:
        f.write(str(checked))

def pithon(code):
    global result
    try:
        local_vars = {}
        exec(code, {}, local_vars)  # Используем локальный словарь для хранения переменных
        return local_vars.get('result')  # Возвращаем значение переменной result
    except Exception as e:
        return e

def load_checked():
    with open("checked_domains.txt", "r") as f:
        return pithon(f"import numpy as np\nresult = np.array({f.read()})")

def normal_filename(link):
    return "screenshots/" + link.replace("https://", "").replace("http://", "").replace("/", "_").replace(":", "_").replace("?", '').replace('=','').replace('%','') + ".png"

def process_link(driver, link):
    try:
        # # options = webdriver.ChromeOptions()

        # options = Options()
        # options.add_argument("--log-level=3")
        # options.add_argument("--disable-software-rasterizer")
        # options.add_argument("--headless")
        # options.add_argument("--start-maximized")

        # #driver = webdriver.Chrome(options=options)


        # driver = webdriver.Firefox(options=options)

        domain = get_domain(link)

        if not domain in checked:
            output = normal_filename(link)
            # pass
            if os.path.exists(output):
                os.remove(output)

            driver.get(link)
            title = driver.title
            driver.save_screenshot(output)

            checked = np.append(checked, domain)

            # driver.quit()
            print(f"Скриншот сохранен как {output}")
        else:
            print('pass...')
            return None

        return {"url": link, "title": title, "screenshot": output, "domain": get_domain(link)}, checked
    except:
        return None

def process_links(links):
    results = []

    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--headless")
    options.add_argument("--start-maximized")

    driver = webdriver.Firefox(options=options)

    for link in links:
        temp_result = process_link(driver, link)
        if temp_result: results.append(temp_result)

    driver.quit()
    return results

if __name__ == "__main__":
    links = ["https://google.com", "https://amazon.com", "https://yandex.ru", "https://minilink.pro"]

    data = process_links(links)
    for el in data:
        print(el)
