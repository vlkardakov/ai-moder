from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()

options.add_argument("--log-level=3")
options.add_argument("--disable-software-rasterizer")
options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--incognito")

ffox_driver = webdriver.Firefox( options=options, service=serv )
ffox_driver.get('https://minilink.pro')
print(ffox_driver.title)