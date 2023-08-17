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

    browser.get("https://suninjuly.github.io/math.html")

    rb=browser.find_element(By.CSS_SELECTOR, '[id="peopleRule"]')
    radio=rb.get_attribute("checked")
    print(rb.get_attribute("checked"))
    assert radio is not None, "значит не стоит как дефаулт"



    
    

finally:
    time.sleep(40)
    browser.quit()
