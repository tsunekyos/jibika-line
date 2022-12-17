from selenium import webdriver
from selenium.webdriver.common.by import By

def click_element(driver, by, value):
    element = driver.find_element(by, value)
    element.click()

def click_element_by_id(driver, id):
    click_element(driver, By.ID, id)

def click_element_by_xpath(driver, xpath):
    click_element(driver, By.XPATH, xpath)
    
def send_keys_by_xpath(driver, xpath, text):
    element = driver.find_element(By.XPATH, xpath)
    element.send_keys(text)