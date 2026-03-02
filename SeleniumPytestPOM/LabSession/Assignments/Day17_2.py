# 2. Write an automation script in selenium python to search flights in make my
# trip.com and validate that the user is on the correct redirected page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from datetime import datetime, timedelta
import time

departure_day= 5


# -------- Setup --------
driver:WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 25)

driver.get("https://www.makemytrip.com/")

wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='commonModal__close']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//img[@alt='minimize']"))).click()

wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='fromCity']"))).send_keys("Lucknow")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='toCity']"))).send_keys("New Delhi")
driver.find_element(By.XPATH,"//label[@for='departure']").click()
#wait.until(EC.element_to_be_clickable((By.XPATH,"//img[@alt='minimize']"))).click()
time.sleep(3)
# Generate future date
future_date = datetime.now() + timedelta(days=departure_day)
formatted_date = future_date.strftime("%a %b %d %Y")

print("Selecting Date:", formatted_date)
# Open calendar
#wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='departure']"))).click()
# Click date
date_xpath = f"//div[@aria-label='{formatted_date}']"
wait.until(EC.element_to_be_clickable((By.XPATH, date_xpath))).click()

driver.find_element(By.XPATH,"//label[@for='travellers']").click()
wait.until(EC.visibility_of_any_elements_located((By.XPATH,"//button[normalize-space()='APPLY']")))
driver.find_element(By.XPATH,"//body/div[@id='root']/div[@id='top-banner']/div[@class='minContainer']/div/div[@class='flightWidgetSection appendBottom40']/div[@class='flightSearchWidget']/div[@class='searchWidgetContainer ']/div[@class='fltWidgetSection appendBottom40 primaryTraveler ']/div[@class='fsw widgetOpen']/div[@class='fsw_inner returnPersuasion']/div[@class='flt_fsw_inputBox flightTravllers inactiveWidget activeWidget']/div[@class='fltTravellers gbTravellers']/div[@class='appendBottom20']/ul[@class='guestCounter font12 darkText gbCounter']/li[1]").click()
driver.find_element(By.XPATH,"//li[normalize-space()='Premium Economy']").click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='APPLY']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//div[normalize-space()='Student']"))).click()
driver.find_element(By.XPATH,"//a[normalize-space()='Search']").click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='okayButton fontSize16']"))).click()
# ---------------- VALIDATION ----------------
wait.until(EC.url_contains("flight/search"))

assert "flight/search" in driver.current_url
print("✅ Successfully redirected to Flight Search Results Page")

time.sleep(3)

driver.close()


# ---------------- FROM CITY ----------------
# from_city = wait.until(EC.element_to_be_clickable((By.ID, "fromCity")))
# from_city.click()
#
# from_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='From']")))
# from_input.send_keys("Lucknow")
#
# wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Lucknow, India')]"))).click()
#
# # ---------------- TO CITY ----------------
# to_city = wait.until(EC.element_to_be_clickable((By.ID, "toCity")))
# to_city.click()
#
# to_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='To']")))
# to_input.send_keys("New Delhi")
#
# wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'New Delhi, India')]"))).click()
#
# # ---------------- SELECT DATE ----------------
# wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='departure']"))).click()
#
# future_date = datetime.now() + timedelta(days=departure_day)
# formatted_date = future_date.strftime("%a %b %d %Y")
#
# print("Selecting Date:", formatted_date)
#
# date_xpath = f"//div[@aria-label='{formatted_date}']"
# wait.until(EC.element_to_be_clickable((By.XPATH, date_xpath))).click()

