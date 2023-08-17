import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#browser = webdriver.Chrome()

@pytest.fixture(scope="module")
def browser():
    print("start browser")
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = 'yandexdriver.exe'
    browser = webdriver.Chrome(binary_yandex_driver_file, options=options)
    yield browser
    print("close browser")
    browser.quit()

@pytest.mark.smoke
class TestReg():
    def test_reg1(self, browser):
        browser.get("http://suninjuly.github.io/registration1.html")
        first_name=browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        first_name.send_keys("Mikhail")
        last_name=browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        last_name.send_keys("Kentovich")
        mail=browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        mail.send_keys("mikhail@soba4ka.ru")


        button=browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        congratulations=browser.find_element(By.TAG_NAME, "h1")
        congra_text=congratulations.text
        assert "Congratulations! You have successfully registered!"==congra_text, "error"

    def test_reg2(self, browser):
        browser.get("http://suninjuly.github.io/registration2.html")

        first_name=browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        first_name.send_keys("Mikhail")
        last_name=browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        last_name.send_keys("Kentovich")
        mail=browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        mail.send_keys("mikhail@soba4ka.ru")


        button=browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        congratulations=browser.find_element(By.TAG_NAME, "h1")
        congra_text=congratulations.text
        assert "Congratulations! You have successfully registered!"==congra_text, "error"
@pytest.mark.ggl
def test_ggl(browser):
    browser.get("http://python.org")
    assert browser.title=="Welcome to Python.org", "wrong url"
if __name__=="__main__":
    pytest.main()