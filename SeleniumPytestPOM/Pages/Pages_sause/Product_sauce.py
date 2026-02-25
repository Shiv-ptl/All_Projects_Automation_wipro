from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    add_to_cart_product1= (By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_product2 = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    page_title = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart_product1)).click()
        #self.wait.until(EC.element_to_be_clickable(self.add_to_cart_product2)).click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()

    def get_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.page_title)).text