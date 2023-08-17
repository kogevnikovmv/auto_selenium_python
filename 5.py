import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = 'yandexdriver.exe'
    browser = webdriver.Chrome(binary_yandex_driver_file, options=options)

    browser.get("http://suninjuly.github.io/registration2.html")

    first_name=browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    first_name.send_keys("Mikhail")
    last_name=browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    last_name.send_keys("Kentovich")
    mail=browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    mail.send_keys("mikhail@soba4ka.ru")


    button=browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    
    time.sleep(20)

    congratulations=browser.find_element(By.TAG_NAME, "h1")
    congra_text=congratulations.text
    assert "Congratulations! You have successfully registered!"==congra_text

finally:
    time.sleep(30)
    browser.quit()
