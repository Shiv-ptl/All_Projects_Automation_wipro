from datetime import datetime
import os
import tempfile
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager




"""
@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()

    # ⭐ create temporary clean profile
    temp_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_dir}")

    # disable password services
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }

    options.add_experimental_option("prefs", prefs)

    # ⭐ disable ALL password related features
    options.add_argument("--disable-features=PasswordCheck")
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--disable-features=PasswordManagerOnboarding")

    # disable chrome UI
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-blink-features=AutomationControlled")

    options.add_argument("--start-maximized")

    # service = Service(ChromeDriverManager().install())
    #driver: WebDriver = webdriver.Firefox(service=Service(ChromeDriverManager().install()
    driver:WebDriver=webdriver.Chrome(service = Service(ChromeDriverManager().install()),options=options)
    #driver = webdriver.Chrome()


    #driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)



    yield driver
    driver.quit()
"""
"""
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="function")
def driver():
    options = webdriver.FirefoxOptions()
    options.set_preference("signon.rememberSignons", False)
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    #driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

"""
"""
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
@pytest.fixture(scope="function")
def driver():
    options = webdriver.EdgeOptions()
    options.add_argument("--disable-notifications")

    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

"""


@pytest.fixture(scope="function")
def driver():
    options = webdriver.FirefoxOptions()

    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=options
    )

    yield driver
    driver.quit()


# screenshot hook  taking if  the test case fails
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(file_path)

# @pytest.fixture(hookwrapper =True)
# def pytest_runtest_makereport(item,call):
#     outcome = yield
#     report = outcome.get_result()
#
#     if report.when == "call" and report.failed:
#         driver = item.funcargs.get("driver",None)
#         if driver:
#             screenshots_dir = "screenshots"
#             os.makedirs()

# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#
#     yield driver
#     driver.quit()

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



