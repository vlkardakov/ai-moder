from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()
options.add_argument("--log-level=3")
options.add_argument("--disable-software-rasterizer")
options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--incognito")


service = Service('venv/bin/geckodriver')


driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.example.com")
print(driver.title)
driver.quit()
