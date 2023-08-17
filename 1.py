import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = 'yandexdriver.exe'
    browser = webdriver.Chrome(binary_yandex_driver_file, options=options)

    browser.get("http://suninjuly.github.io/simple_form_find_task.html")

    first_name=browser.find_element(By.NAME, "first_name")
    first_name.send_keys("Mikhail")
    last_name=browser.find_element(By.NAME, "last_name")
    last_name.send_keys("Kentovich")
    city=browser.find_element(By.NAME, "firstname")
    city.send_keys("Saratov")
    country=browser.find_element(By.ID, "country")
    country.send_keys("Middleearth")
    button=browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
