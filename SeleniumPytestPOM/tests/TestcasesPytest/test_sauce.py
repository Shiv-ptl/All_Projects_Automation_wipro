import time
import pytest
from Pages.Pages_sause.login_Sause import LoginPage
from Pages.Pages_sause.Product_sauce import ProductsPage
from Pages.Pages_sause.cart_sauce import CartPage
from Pages.Pages_sause.checkout_sauce import CheckoutPage
from Pages.Pages_sause.Validate_checkout import Valid_checkout


from utilities.excel_utils import get_excel_data

from utilities.logger import get_logger
test_data = get_excel_data("C:/Users/LENOVO/PycharmProjects/All_Projects_Automation_wipro/SeleniumPytestPOM/testdata/login_data_sauce.xlsx", "Sheet1")
logger = get_logger()
class TestSauceLogin:

    @pytest.mark.parametrize("username,password", test_data)
    def test_login_users(self, driver, username, password):
        logger.info("Opening application")

        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)
        logger.info("Entering the credentials")
        login.login(username, password)

        if username == "locked_out_user":
            assert "Epic sadface" in driver.page_source
        else:
            assert "inventory" in driver.current_url


class Test_CheckoutFlow:

    def test_complete_order(self, driver):
        logger.info("Opening application")
        driver.get("https://www.saucedemo.com/")

        # login
        login = LoginPage(driver)
        logger.info("Entering the credentials")
        login.login("standard_user", "secret_sauce")


        # add item
        products = ProductsPage(driver)
        products.add_backpack_to_cart()
        products.go_to_cart()
        time.sleep(5)

        # cart
        cart = CartPage(driver)
        time.sleep(5)
        assert cart.get_cart_item() == "Sauce Labs Backpack"
        cart.click_checkout()

        # checkout
        checkout = CheckoutPage(driver)
        time.sleep(5)
        checkout.enter_checkout_info("Shivanshu", "Patel", "209868")
        checkout.click_continue()
        time.sleep(5)

        checkout.click_finish()
        time.sleep(5)

        #validate
        valid=Valid_checkout(driver)
        valid.Validate_Thanks()
        time.sleep(3)
        valid.Back_to_Home()
        time.sleep(3)
