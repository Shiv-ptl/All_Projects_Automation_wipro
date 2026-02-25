import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def test_demowebshop_flow():

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()

    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(2)

    # ---------- REGISTER ----------
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(2)

    driver.find_element(By.ID, "gender-male").click()
    driver.find_element(By.ID, "FirstName").send_keys("Test")
    driver.find_element(By.ID, "LastName").send_keys("User")

    email = f"testuser{int(time.time())}@mail.com"
    driver.find_element(By.ID, "Email").send_keys(email)

    driver.find_element(By.ID, "Password").send_keys("Test@123")
    driver.find_element(By.ID, "ConfirmPassword").send_keys("Test@123")

    driver.find_element(By.ID, "register-button").click()
    time.sleep(2)

    # Logout
    driver.find_element(By.LINK_TEXT, "Log out").click()
    time.sleep(2)

    # ---------- LOGIN ----------
    driver.find_element(By.LINK_TEXT, "Log in").click()
    time.sleep(2)

    driver.find_element(By.ID, "Email").send_keys(email)
    driver.find_element(By.ID, "Password").send_keys("Test@123")

    driver.find_element(By.CSS_SELECTOR, "input.login-button").click()
    time.sleep(2)

    # ---------- ADD PRODUCT ----------
    driver.find_element(By.LINK_TEXT, "Books").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "(//input[@value='Add to cart'])[1]").click()
    time.sleep(2)

    # ---------- VERIFY CART ----------
    cart_qty = driver.find_element(By.CSS_SELECTOR, ".cart-qty").text
    print("Cart Quantity:", cart_qty)

    assert "(1)" in cart_qty

    # ---------- OPEN CART ----------
    driver.find_element(By.LINK_TEXT, "Shopping cart").click()
    time.sleep(2)

    assert "Shopping cart" in driver.page_source

    driver.quit()