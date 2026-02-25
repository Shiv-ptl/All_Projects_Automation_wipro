from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn = (By.ID, "finish")
    success_msg = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_checkout_info(self, fname, lname, zip_code):
        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(zip_code)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_btn)).click()

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.finish_btn)).click()

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.success_msg)).text