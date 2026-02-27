from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -------- Setup --------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 25)

driver.get("https://phptravels.net/signup?type=agent")

# -------- First Name --------
wait.until(EC.visibility_of_element_located((By.NAME, "first_name"))).send_keys("shiv")

# -------- Last Name --------
driver.find_element(By.NAME, "last_name").send_keys("ptl")

# -------- Email --------
driver.find_element(By.NAME, "email").send_keys("shiv12ptl@gmail.com")

# -------- Phone --------
#phone = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Phone']")))
#phone.send_keys("9999999999")

# -------- Password --------
driver.find_element(By.NAME, "password").send_keys("Test@1234")

# -------- Confirm Password --------
driver.find_element(By.NAME, "password_confirmation").send_keys("Test@1234")

# -------- Submit --------
signup_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Signup')]")))
signup_btn.click()

print("Agent signup form submitted successfully!")

time.sleep(5)
driver.quit()