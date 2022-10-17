from requests import options
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com")
print(driver.title)