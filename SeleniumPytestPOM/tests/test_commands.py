import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_Browser:

    def test_navigation(self):

        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()

        driver.get("https://trytestingthis.netlify.app/")
        time.sleep(2)

        title = driver.title
        print(title)

        url = driver.current_url
        print(url)

        driver.back()
        time.sleep(2)

        driver.forward()
        time.sleep(2)

        driver.refresh()

        driver.quit()