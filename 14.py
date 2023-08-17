import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math



options = webdriver.ChromeOptions()
binary_yandex_driver_file = 'yandexdriver.exe'
browser = webdriver.Chrome(binary_yandex_driver_file, options=options)
browser.implicitly_wait(5)

try:    
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button=browser.find_element(By.CSS_SELECTOR, ".trollface.btn")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    windows=browser.window_handles
    new_window=windows[1]

    browser.switch_to.window(new_window)
    
    
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
