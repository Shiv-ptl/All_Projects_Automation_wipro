import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager


class Test_Browser:

    def test_navigation(self):

        driver: WebDriver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()

        driver.get("https://jqueryui.com/datepicker/")
        driver.implicitly_wait(10)

        frame = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
        driver.switch_to.frame(frame)

        #driver.switch_to.frame(0)  # switch by index

        datepicker = driver.find_element(By.XPATH,"//input[@id='datepicker']")
        datepicker.click()
        time.sleep(5)
        driver.close()