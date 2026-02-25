
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v143.dom import scroll_into_view_if_needed
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.expected_conditions import title_is
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

BASE_URL = "https://rahulshettyacademy.com/seleniumPractise/#/"
ITEMS_TO_ADD = ["Cucumber", "Brocolli", "Beetroot"]

class BookVegies:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        try:
            self.driver.get(BASE_URL)
            print("Opened  URL")
        except Exception as e:
            print(f"Error opening URL: {e}")



    def add_to_cart(self,items):
        products = self.driver.find_elements(By.XPATH, "//h4[@class='product-name']")
        added_items = []

        for product in products:
            product_name = product.text.split("-")[0].strip()

            if product_name in ITEMS_TO_ADD:
                add_button = product.find_element(By.XPATH, "following-sibling::div/button")
                add_button.click()
                added_items.append(product_name)

        return added_items

    def open_cart(self):
        self.driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()

    def proceed_checkout(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']").click()

    def place_order(self):
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Place Order']").click()
        time.sleep(4)
        country_add = Select(self.driver.find_element(By.XPATH,"//div[@class='wrapperTwo']//div//select"))
        country_add.select_by_visible_text("India")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Proceed']").click()
        success_msg = self.driver.find_element(By.CSS_SELECTOR, ".wrapperTwo").text

        print(success_msg)

        assert "Thank you" in success_msg




def test_add_items_and_checkout():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    try:
        page = BookVegies(driver)

        page.open()

        added_items = page.add_to_cart(ITEMS_TO_ADD)

        assert len(added_items) == len(ITEMS_TO_ADD)

        page.open_cart()

        page.proceed_checkout()
        page.place_order()

        #assert "checkout" in driver.current_url.lower()

    finally:
        driver.quit()
