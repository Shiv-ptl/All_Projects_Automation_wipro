

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def setup(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    #driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)


    request.cls.driver = driver
    yield
    driver.quit()




# pages - Contains all Pages for action
# Addtocart - Page class for addtocart functionality.
# Checkout - Page class for checkout process
# Loginp - Page class for login page process
# Products_page - Page class for products page
# tests- Contains all test files.
# test_login - Test cases for login prcoess
# utilities- Helpes for reading/writing data
# ReadExcel- Reads test data from Excel file
# WriteToexcel - Writes test data to Excel file
# conftest- Pytest fixtures setup and teardown , browser
# requirements.txt - forrequired Python packages
#pytest.ini-for configuration like report gen



