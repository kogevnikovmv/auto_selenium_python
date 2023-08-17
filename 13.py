import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math



options = webdriver.ChromeOptions()
binary_yandex_driver_file = 'yandexdriver.exe'
browser = webdriver.Chrome(binary_yandex_driver_file, options=options)

try:    
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button=browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    confirm=browser.switch_to.alert
    confirm.accept()
    
    xx=browser.find_element(By.ID, "input_value")
    x=int(xx.text)

    f=math.log(abs(12*math.sin(x)))

    ans=browser.find_element(By.ID, "answer")
    ans.send_keys(f)

    submit=browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()
    
    


finally:
    time.sleep(40)
    browser.quit()
