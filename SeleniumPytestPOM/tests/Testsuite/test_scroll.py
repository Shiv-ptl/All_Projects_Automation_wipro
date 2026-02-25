import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_Scroll:
    def test_scroll(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()

        driver.get("https://www.amazon.in/")
        time.sleep(3)
        amz = driver.find_element(By.XPATH,"//a[normalize-space()='Amazon Pay on Merchants']")

        driver.execute_script("arguments[0].scrollIntoView();",amz)

        time.sleep(3)
        #amz.click()


        #verticle up scroll - x coordinate should be zero

        driver.execute_script("window.scrollBy(0,-3000)")
        time.sleep(3)

        #horizontal down scroll
        driver.execute_script("window.scrollBy(0,5000)")
        time.sleep(3)

        driver.close()

