import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v143.dom import scroll_into_view_if_needed
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


# class Test_multiselectRadio:
#     def test_multiselectradio(self):
#         driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#         driver.maximize_window()
#         driver.get('https://rahulshettyacademy.com/AutomationPractice/')
#
#         time.sleep(4)
#         # element = driver.find_element(By.XPATH, "//div[@class='form-check form-check-inline']//input[@type='checkbox']")
#         # driver.execute_script("arguments[0].scrollIntoView();", element)
#         checkbox_list = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
#         count = len(checkbox_list)
#         print(count)
#
#         #iterate the list
#         for i in checkbox_list:
#             time.sleep(2)
#             i.click()
#
#
#         time.sleep(3)
#         #close only the current browser
#         driver.close()
#
# class Test_multiselectRadio2:
#     def test_multiselectradio2(self):
#         driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#         driver.maximize_window()
#         driver.get('https://testautomationpractice.blogspot.com/')
#
#         time.sleep(4)
#         element = driver.find_element(By.XPATH, "//div[@class='form-check form-check-inline']//input[@type='checkbox']")
#         driver.execute_script("arguments[0].scrollIntoView();", element)
#         checkbox_list = driver.find_elements(By.XPATH,"//div[@class='form-check form-check-inline']//input[@type='checkbox']")
#         count = len(checkbox_list)
#         print(count)
#
#         #iterate the list
#         for i in checkbox_list:
#             time.sleep(2)
#             i.click()
#
#
#         time.sleep(3)
#         #close only the current browser
#         driver.close()


class Test_multiselectRadio3:
    def test_multiselectradio3(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList')

        time.sleep(4)
        name = driver.find_element(By.NAME, "username")
        name.send_keys("Admin")

        password = driver.find_element(By.NAME, "password")
        password.send_keys("admin123")

        time.sleep(4)

        Login = driver.find_element(By.XPATH, "//button[@type='submit']")
        Login.click()
        time.sleep(5)


        checkbox_list = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//input[@type='checkbox']")   #//i[@class = 'oxd-icon bi-check oxd-checkbox-input-icon']
        count =len(checkbox_list)

        print("Total checkboxes:", count)

        for checkbox in checkbox_list:
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", checkbox)
            #
            time.sleep(1)
            #
            driver.execute_script("arguments[0].click();", checkbox)


        time.sleep(3)
        #close only the current browser
        driver.close()



