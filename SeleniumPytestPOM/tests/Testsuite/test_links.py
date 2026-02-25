import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

Download_dir = "C://Users//LENOVO//Downloads"
class Test_links:
    def test_link(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()

        driver.get("https://the-internet.herokuapp.com/download")
        time.sleep(3)

        links =driver.find_elements(By.TAG_NAME,"a")
        count=len(links)
        print(count)

        for link in links:
            print(link.text)

        time.sleep(3)
        driver.close()