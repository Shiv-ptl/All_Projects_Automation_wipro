import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    yield driver
    driver.quit()




def test_full_banking_flow(driver):

    wait = WebDriverWait(driver, 10)


    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Bank Manager Login']"))).click()


    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add Customer')]"))).click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Shivanshu")
    driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Patel")
    driver.find_element(By.XPATH, "//input[@placeholder='Post Code']").send_keys("209868")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    # Handle Alert
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()


    driver.find_element(By.XPATH, "//button[contains(text(),'Open Account')]").click()
    time.sleep(2)

    Select(driver.find_element(By.ID, "userSelect")).select_by_visible_text("Shivanshu Patel")
    Select(driver.find_element(By.ID, "currency")).select_by_visible_text("Dollar")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    wait.until(EC.alert_is_present())
    driver.switch_to.alert.accept()


    driver.find_element(By.XPATH, "//button[text()='Home']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Customer Login']").click()
    time.sleep(2)

    Select(driver.find_element(By.ID, "userSelect")).select_by_visible_text("Shivanshu Patel")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(2)


    driver.find_element(By.XPATH, "//button[contains(text(),'Deposit')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder='amount']").send_keys("5000")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()


    balance = driver.find_element(By.XPATH, "//strong[@class='ng-binding'][2]").text
    assert balance == "5000"


    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Withdrawl')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder='amount']").send_keys("1000")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()


    balance = driver.find_element(By.XPATH, "//strong[@class='ng-binding'][2]").text
    assert balance == "4000"