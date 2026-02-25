import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_Actions:
    def test_dragdrop(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()

        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        time.sleep(3)

        action = ActionChains(driver)
        time.sleep(3)
        source = driver.find_element(By.XPATH,"//div[@id='column-a']")
        dest = driver.find_element(By.XPATH,"//div[@id='column-b']")

        action.drag_and_drop(source,dest)
        time.sleep(3)
        driver.close()
