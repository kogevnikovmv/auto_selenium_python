import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = 'yandexdriver.exe'
    browser = webdriver.Chrome(binary_yandex_driver_file, options=options)

    browser.get("http://suninjuly.github.io/huge_form.html")
    elements=browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for element in elements:
        element.send_keys("prrr")

    button=browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    

finally:
    time.sleep(60)
    browser.quit()
