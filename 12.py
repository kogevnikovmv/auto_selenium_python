import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


try:
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = 'yandexdriver.exe'
    browser = webdriver.Chrome(binary_yandex_driver_file, options=options)


    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    first = browser.find_element(By.NAME, 'firstname')
    first.send_keys("Clark")
    second=browser.find_element(By.NAME, 'lastname')
    second.send_keys("Kent")
    mail=browser.find_element(By.NAME, 'email')
    mail.send_keys("superman@smallville.com")
    send_file=browser.find_element(By.ID, "file")
    cur_dir=os.path.abspath(os.path.dirname(__file__))
    file=os.path.join(cur_dir, 'ya_ne_superman.txt')
    send_file.send_keys(file)
    button=browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    


finally:
    time.sleep(40)
    browser.quit()
