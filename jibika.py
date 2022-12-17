from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import config

def seleniumTest():
    driver = webdriver.Chrome()
    driver.get(config.WEBSITE_URL)

    sleep(5)
    driver.quit()


seleniumTest()