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

        driver.get("https://the-internet.herokuapp.com/tables")
        driver.implicitly_wait(10)

        #no of rows
        rows = driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr")
        for i in rows:
            print(i.text)

        time.sleep(4)

        #colmns

        cols = driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr[1]/td")
        for i in cols:
            print(i.text)

        time.sleep(4)

        #fetch the cell data
        celldata = driver.find_element(By.XPATH,"//table[@id='table1']//tr[3]//td[4]")
        assert  "$100.00" in celldata.text

        time.sleep(4)
        driver.close()