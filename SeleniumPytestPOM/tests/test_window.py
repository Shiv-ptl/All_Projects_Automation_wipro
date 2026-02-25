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

        driver.get("https://the-internet.herokuapp.com/windows")
        time.sleep(2)
        driver.implicitly_wait(10)

        clickhere = driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']")
        clickhere.click()
        #fetch the window handles of both tabs
        window = driver.window_handles
        print(window)
        #move the control to the child window
        driver.switch_to.window(window[1])

        text = driver.find_element(By.XPATH,"//h3[normalize-space()='New Window']")
        print(text)
        time.sleep(3)
        driver.close()

        #get back to parent window
        driver.switch_to.window(window[0])
        clickhere.is_displayed()
        time.sleep(3)

        driver.close()




