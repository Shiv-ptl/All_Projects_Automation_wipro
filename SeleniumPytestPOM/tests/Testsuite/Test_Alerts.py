import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v143.dom import scroll_into_view_if_needed
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager


class Test_alerts:
    def test_alerts(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/javascript_alerts')

        simlealert = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
        simlealert.click()
        time.sleep(2)
        alt = driver.switch_to.alert
        alt.accept()
        time.sleep(2)

        confalert = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']")
        confalert.click()
        alt = driver.switch_to.alert
        time.sleep(2)
        alt.dismiss()
        time.sleep(2)

        promptalt = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
        promptalt.click()
        alt=driver.switch_to.alert
        alerttext = alt.text
        print(alerttext)
        alt.send_keys("Test Hello")
        alt.accept()
        time.sleep(3)

        driver.close()


