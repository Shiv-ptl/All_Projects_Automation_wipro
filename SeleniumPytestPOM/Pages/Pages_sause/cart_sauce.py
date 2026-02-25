from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    checkout_button = (By.ID, "checkout")
    cart_item = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_checkout(self):
        btn=self.wait.until(EC.element_to_be_clickable(self.checkout_button))
        self.driver.execute_script("arguments[0].click();", btn)

    def get_cart_item(self):
        return self.wait.until(EC.visibility_of_element_located(self.cart_item)).text