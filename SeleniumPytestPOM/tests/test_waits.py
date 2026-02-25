import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v143.dom import scroll_into_view_if_needed
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys


# https://www.selenium.dev/documentation/webdriver/waits/

class Test_waits:
    def test_waits(self):
        driver: WebDriver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        #
        driver.implicitly_wait(2)

        #explicit wait
        radio_btn = driver.find_element(By.XPATH,"(//input[@value='radio1'])[1]")
        wait = WebDriverWait(driver,timeout=2)
        wait.until(lambda _: radio_btn.is_displayed())

        #custom wait or fluent wait
        errors = [NoSuchElementException, ElementNotInteractableException]
        wait = WebDriverWait(driver,timeout=2,poll_frequency=.2,ignored_exceptions=errors)
        wait.until(lambda _: radio_btn.send_keys("Displayed")or True)



        time.sleep(4)


        radio3 = driver.find_element(By.XPATH, "//input[@value='radio3']")
        radio3.click()

        driver.close()