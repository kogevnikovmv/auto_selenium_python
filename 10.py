import time
from selenium import webdriver
from selenium.webdriver.common.by import By



#28.945883663396053


try:
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = 'yandexdriver.exe'
    browser = webdriver.Chrome(binary_yandex_driver_file, options=options)


    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(40)
    browser.quit()
