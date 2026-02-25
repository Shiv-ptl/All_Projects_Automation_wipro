import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v143.dom import scroll_into_view_if_needed
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.expected_conditions import title_is
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
IMPLICIT_WAIT = 10

#
# class Test_alerts:
#     def test_alerts(self):
#         driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#         driver.maximize_window()
#         driver.get(BASE_URL)

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self):
        try:
            self.driver.get(BASE_URL)
            print("Opened SauceDemo URL")
        except Exception as e:
            print(f"Error opening URL: {e}")

    def login(self):
        try:
            self.driver.find_element(*self.username_input).send_keys(USERNAME)
            self.driver.find_element(*self.password_input).send_keys(PASSWORD)
            self.driver.find_element(*self.login_button).click()
            print("Login successful")
        except Exception as e:
            print(f"Login failed: {e}")

    def get_error_message(self):
        try:
            return self.driver.find_element(*self.error_message).text
        except:
            return None

def test_ValidLogin():
        driver = None
        try:
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.implicitly_wait(IMPLICIT_WAIT)

            login_page = LoginPage(driver)


            login_page.open()
            login_page.login()

            time.sleep(2)

            error = login_page.get_error_message()

            if error:
                print("Login failed:", error)
            else:
                print("Login successful — redirected to products page")

        except Exception as e:
            print(f"Test execution error: {e}")






