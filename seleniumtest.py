from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()
service = Service('venv/bin/geckodriver')

driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.example.com")
print(driver.title)
driver.quit()
