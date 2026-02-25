import  time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

time.sleep(4)
name = driver.find_element(By.ID,"user-name")
name.send_keys("standard_user")

password = driver.find_element(By.ID,"password")
password.send_keys("secret_sauce")

time.sleep(4)

Login= driver.find_element(By.ID,"login-button")
Login.click()
time.sleep(5)


#assert "OrangeHRM" in driver.title
# #Check dashboard
# dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']")
#
# if dashboard.is_displayed():
#     print("Login Successful — Dashboard is visible")
# else:
#     print("Dashboard not visible")
#
driver.quit()