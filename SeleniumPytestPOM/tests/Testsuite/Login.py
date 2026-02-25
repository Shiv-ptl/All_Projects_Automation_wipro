import  time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
class Test_login:
    def login():
        driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        time.sleep(4)
        name = driver.find_element(By.NAME,"username")
        name.send_keys("Admin")

        password = driver.find_element(By.NAME,"password")
        password.send_keys("admin123")

        time.sleep(4)

        Login= driver.find_element(By.XPATH,"//button[@type='submit']")
        Login.click()
        time.sleep(5)


        assert "OrangeHRM" in driver.title
# #Check dashboard
# dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']")
#
# if dashboard.is_displayed():
#     print("Login Successful — Dashboard is visible")
# else:
#     print("Dashboard not visible")
#
    #driver.quit()

