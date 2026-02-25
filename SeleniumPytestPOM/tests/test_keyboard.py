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

        driver.get("https://www.instagram.com/accounts/login")
        time.sleep(3)

        action = ActionChains(driver)
        email = driver.find_element(By.XPATH,"//input[@name='email']")
        seriesofactions = action.move_to_element(email).key_down(Keys.SHIFT).send_keys("Hello").key_up(Keys.SHIFT).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).send_keys(Keys.TAB).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL)
        seriesofactions.perform()
        # show=driver.find_element(By.XPATH,"//div[@aria-label='Hide password']")
        # show.click()
        time.sleep(3)
        driver.close()