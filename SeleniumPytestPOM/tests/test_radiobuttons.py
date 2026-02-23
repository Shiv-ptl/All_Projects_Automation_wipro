import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v143.dom import scroll_into_view_if_needed
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_login:
    def test_radio1(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get('https://rahulshettyacademy.com/AutomationPractice/')

        time.sleep(4)

        time.sleep(4)
        # click on login button
        # radio1 = driver.find_element(By.XPATH,"//input[@value='radio1']")
        # radio1.click()
        # radio2 = driver.find_element(By.XPATH, "//input[@value='radio2']")
        # radio2.click()
        radio3 = driver.find_element(By.XPATH, "//input[@value='radio3']")
        radio3.click()

class Test_radio2:
    def test_radio2(self):
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            driver.maximize_window()
            driver.get('https://testautomationpractice.blogspot.com/')

            time.sleep(4)

            time.sleep(4)
            # click on login button
            gender = driver.find_element(By.ID, "male")
            gender.click()

            days = driver.find_element(By.ID,"friday")
            days.click()


