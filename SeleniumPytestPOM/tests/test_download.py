import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

Download_dir = "C://Users//LENOVO//Downloads"
class Test_Download:
    def test_download(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()

        driver.get("https://the-internet.herokuapp.com/download")
        time.sleep(3)

        action = ActionChains(driver)
        alert =driver.find_element(By.XPATH,"//a[normalize-space()='alert.jpeg']")
        alert.click()

        file_path = os.path.join(Download_dir,"alert.jpeg")
        assert os.path.exists(file_path)

        time.sleep(3)
        driver.close()
