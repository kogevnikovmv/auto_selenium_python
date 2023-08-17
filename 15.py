import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math



options = webdriver.ChromeOptions()
binary_yandex_driver_file = 'yandexdriver.exe'
browser = webdriver.Chrome(binary_yandex_driver_file, options=options)
browser.implicitly_wait(5)

try:    
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    
    button=browser.find_element(By.ID, "book")
    pprice = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    button.click()

    xx=browser.find_element(By.ID, "input_value")
    x=int(xx.text)

    f=math.log(abs(12*math.sin(x)))

    ans=browser.find_element(By.ID, "answer")
    ans.send_keys(f)

    submit=browser.find_element(By.ID, "solve")
    submit.click()
    
    


finally:
    time.sleep(40)
    browser.quit()
