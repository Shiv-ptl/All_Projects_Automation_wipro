import time
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "wrong_password"   # change to test failure
IMPLICIT_WAIT = 10


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self):
        self.driver.get(BASE_URL)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        try:
            return self.driver.find_element(*self.error_message).text
        except:
            return None


def test_login_validation():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(IMPLICIT_WAIT)

    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(USERNAME, PASSWORD)

    time.sleep(2)

    error = login_page.get_error_message()

    if error:
        print("❌ Login failed:", error)
    else:
        print("✅ Login successful — redirected to products page")

    driver.quit()