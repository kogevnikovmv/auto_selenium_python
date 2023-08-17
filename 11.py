import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math



try:
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = 'yandexdriver.exe'
    browser = webdriver.Chrome(binary_yandex_driver_file, options=options)


    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    xx = browser.find_element(By.ID, "input_value")
    x=int(xx.text)
    f=math.log(abs(12*math.sin(x)))
    otvet=browser.find_element(By.ID, "answer")
    otvet.send_keys(f)
    rchb=browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rchb)
    rchb.click()
    rr=browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rr)
    rr.click()
    button=browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    


finally:
    time.sleep(40)
    browser.quit()
