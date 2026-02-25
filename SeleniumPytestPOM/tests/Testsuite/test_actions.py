import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_Actions:
    def test_action(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()

        driver.get("https://www.amazon.in/")
        time.sleep(3)

        action = ActionChains(driver)

        bestsellers = driver.find_element(By.XPATH,"//a[normalize-space()='Bestsellers']")

        action.double_click(bestsellers).perform()

        time.sleep(3)
        driver.back()
        time.sleep(3)

        mobiles = driver.find_element(By.XPATH,"//a[normalize-space()='Mobiles']")
        action.context_click(mobiles).perform()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        primes = driver.find_element(By.XPATH,"//span[normalize-space()='Prime']")
        action.move_to_element(primes).perform()
        time.sleep(3)


        fresh = driver.find_element(By.XPATH,"//span[normalize-space()='Fresh']")
        action.click_and_hold(fresh).perform()
        time.sleep(2)

        driver.close()