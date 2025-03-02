from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
driver = webdriver.Firefox(options=options)
driver.get("https://www.example.com")
print(driver.title)
driver.quit()