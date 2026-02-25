import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager


class Test_Practice_Page:

    def test_all_features(self):

        driver: WebDriver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()

        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        time.sleep(2)

        click_here = driver.find_element(By.XPATH,"//button[@id='openwindow']")
        click_here.click()

        window = driver.window_handles
        print(window)

        driver.switch_to.window(window[1])
        print("Switched to new window:", driver.title)
        # text = driver.find_element(By.XPATH,"//h1[contains(text(),'Leaders in Automation testing & Software testing t')]")
        # print(text)
        # assert "Leaders in Automation testing & Software testing" in text.text
        time.sleep(3)
        driver.close()

        driver.switch_to.window(window[0])
        click_here.is_displayed()
        time.sleep(3)
        driver.find_element(By.ID, "opentab").click()
        time.sleep(3)

        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        print("Switched to tab:", driver.title)
        driver.close()
        time.sleep(2)

        driver.switch_to.window(window[0])
        time.sleep(2)

        name = "Shivanshu"
        driver.find_element(By.ID, "name").send_keys(name)
        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)

        alert = driver.switch_to.alert
        print("Alert text:", alert.text)
        time.sleep(2)
        alert.accept()


        driver.execute_script("window.scrollBy(0,3000)")
        time.sleep(3)

        rows = driver.find_elements(By.XPATH, "//table[@id='product']//tr")

        for row in rows:
            if "Chennai" in row.text:
                print("Found Chennai row:", row.text)
                assert "Chennai" in row.text
                time.sleep(2)



        action = ActionChains(driver)

        hover = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView();", hover)
        action.move_to_element(hover).perform()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "Top").click()
        time.sleep(2)

        assert "#top" in driver.current_url
        print("URL after clicking Top:", driver.current_url)

        driver.quit()