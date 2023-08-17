import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import math

#28.945883446304432


try:
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = 'yandexdriver.exe'
    browser = webdriver.Chrome(binary_yandex_driver_file, options=options)

    browser.get("http://suninjuly.github.io/selects2.html")

    num1=browser.find_element(By.CSS_SELECTOR, '[id="num1"]')
    a=int(num1.text)
    num2=browser.find_element(By.CSS_SELECTOR, '[id="num2"]')
    b=int(num2.text)
    select=Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(a+b))
    button=browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(40)
    browser.quit()
