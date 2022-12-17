from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import config
import util

def seleniumTest():
    driver = webdriver.Chrome()
    driver.get(config.WEBSITE_URL)

    sleep(2)

    # 確認・キャンセルのリンクをクリック
    util.click_element_by_id(driver, 'aCNF')

    sleep(2)

    util.send_keys_by_xpath(driver, '/html/body/div/form/input[6]', config.WEBSITE_CARD_ID)
    util.send_keys_by_xpath(driver, '/html/body/div/form/input[7]', config.WEBSITE_BIRTHDAY)

    sleep(2)

    util.click_element_by_xpath(driver, '/html/body/div/form/input[8]')
    
    sleep(2)

    # do something

    driver.quit()
    print('seleniumTest finished')

seleniumTest()