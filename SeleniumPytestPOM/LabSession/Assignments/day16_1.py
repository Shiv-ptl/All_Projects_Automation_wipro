#1. Write the automation script to handle the PHP travels using selenium python in the
#below website
#https://phptravels.net/cars
#Add details - Pick-up Location, Drop-off Location and all the other details and search for
# cars functionality
#2. Write an automation script to sign up as a agent in php travels webs ite
#https://phptravels.net/signup?type=agent

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()
# wait = WebDriverWait(driver, 20)
#
# driver.get("https://phptravels.net/cars")
#
# # ---------------- Pick-up Location ----------------
# pickup = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='City or Airport']")))
# pickup.click()
# pickup.send_keys("Lucknow")
# time.sleep(2)
# pickup.send_keys(Keys.ARROW_DOWN)
# pickup.send_keys(Keys.ARROW_DOWN)
# pickup.send_keys(Keys.ENTER)
#
# # WAIT for reload after pickup selection
# time.sleep(3)
#
# # ---------------- Drop-off Location ----------------
# drop = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Same As Pick-up']")))
# drop.click()
#
# # CLEAR existing auto-filled value
# drop.send_keys(Keys.CONTROL + "a")
# drop.send_keys(Keys.DELETE)
#
# # Enter new city
# drop.send_keys("Kanpur")
# time.sleep(2)
# drop.send_keys(Keys.ARROW_DOWN)
# drop.send_keys(Keys.ARROW_DOWN)
# drop.send_keys(Keys.ENTER)
#
# # ---------------- Pick-up Date ----------------
# pickup_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Pick-up Date']")))
# pickup_date.click()
# pickup_day = wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[7]/div[1]")))
#
# # pickup_day = wait.until(EC.element_to_be_clickable(
# #     (By.XPATH, "(//div[contains(@class,'datepicker') and contains(@style,'display: block')]//td[not(contains(@class,'disabled')) and text()='28'])[1]")
# # ))
# pickup_day.click()
#
# # ---------------- Drop-off Date ----------------
# drop_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Return Date']")))
# drop_date.click()
# drop_day = wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[7]/div[1]")))
# # drop_day = wait.until(EC.element_to_be_clickable(
# #     (By.XPATH, "(//div[contains(@class,'datepicker') and contains(@style,'display: block')]//td[not(contains(@class,'disabled')) and text()='20'])[1]")
# # ))
# drop_day.click()
#
# # ---------------- Search Button ----------------
# search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Search')]")))
# search_btn.click()
#
# print("Car search completed successfully!")
#
# time.sleep(5)
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------- Setup ----------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 25)

driver.get("https://phptravels.net/cars")

# ---------- PICKUP LOCATION ----------
pickup = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='City or Airport']")))
pickup.click()
pickup.send_keys("Lucknow")
time.sleep(2)

# Select 2nd suggestion
pickup.send_keys(Keys.ARROW_DOWN)
pickup.send_keys(Keys.ARROW_DOWN)
pickup.send_keys(Keys.ENTER)

# Wait for reload
time.sleep(3)

# ---------- DROP LOCATION ----------
drop = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Same As Pick-up']")))
drop.click()

# Clear auto-filled value
drop.send_keys(Keys.CONTROL + "a")
drop.send_keys(Keys.DELETE)

drop.send_keys("Kanpur")
time.sleep(2)

# Select 2nd suggestion
drop.send_keys(Keys.ARROW_DOWN)
drop.send_keys(Keys.ARROW_DOWN)
drop.send_keys(Keys.ENTER)

# ---------- PICKUP DATE ----------
pickup_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Pick-up Date']")))
pickup_date.click()

wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "datepicker")))

pickup_day = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "(//div[contains(@class,'datepicker') and contains(@style,'display: block')]//td[not(contains(@class,'disabled')) and text()='28'])[last()]")
))
pickup_day.click()

# ---------- DROP DATE ----------
drop_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Return Date']")))
drop_date.click()

wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "datepicker")))

drop_day = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "(//div[contains(@class,'datepicker') and contains(@style,'display: block')]//td[not(contains(@class,'disabled')) and text()='30'])[last()]")
))
drop_day.click()

# ---------- SEARCH ----------
search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Search')]")))
search_btn.click()

print("Car search completed successfully!")

time.sleep(5)
driver.quit()