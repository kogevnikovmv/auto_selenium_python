import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import math

def calc(xx):
  return str(math.log(abs(12*math.sin(int(xx)))))



try:
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = 'yandexdriver.exe'
    browser = webdriver.Chrome(binary_yandex_driver_file, options=options)

    browser.get("http://suninjuly.github.io/get_attribute.html")

    x=browser.find_element(By.CSS_SELECTOR, '[id="treasure"]')
    xx=x.get_attribute('valuex')
    #xx=x.text
    urav=calc(xx)
    pole=browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    pole.send_keys(urav)
    cb=browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
    cb.click()
    rb=browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
    rb.click()


    button=browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    
    

finally:
    time.sleep(40)
    browser.quit()
