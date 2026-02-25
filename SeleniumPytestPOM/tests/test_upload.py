import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys


class Test_Actions:
    def test_dragdrop(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()

        driver.get("https://the-internet.herokuapp.com/upload")
        time.sleep(3)

        action = ActionChains(driver)

        browse = driver.find_element(By.XPATH,"//input[@id='file-upload']")
        browse.send_keys("C:/Users/LENOVO/Desktop/Sessions2.png")
        time.sleep(3)

        upload = driver.find_element(By.XPATH,"//input[@id='file-submit']")

        upload.click()

        time.sleep(3)
        fileupload =driver.find_element(By.XPATH,"//h3[normalize-space()='File Uploaded!']")
        assert fileupload.text =="File Uploaded!"

        time.sleep(3)
        driver.close()