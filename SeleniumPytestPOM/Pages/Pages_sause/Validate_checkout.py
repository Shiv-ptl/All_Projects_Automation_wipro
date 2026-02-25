from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Valid_checkout:
    valid_thanks = (By.XPATH,"//h2[normalize-space()='Thank you for your order!']")
    back_to_home = (By.ID,"back-to-products")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def Validate_Thanks(self):
        msg = self.wait.until(EC.visibility_of_element_located(self.valid_thanks)).text
        print("Displayed:  ",msg)
        assert "Thank you for your order!" in msg

    def Back_to_Home(self):
        self.wait.until(EC.element_to_be_clickable(self.back_to_home)).click()
        assert self.driver.current_url.endswith("inventory.html")

        #assert "inventory.html" in self.driver.current_url