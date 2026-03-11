#1. Write the automation script to handle the PHP travels using selenium python in the
#below website
#https://phptravels.net/cars
#Add details - Pick-up Location, Drop-off Location and all the other details and search for
# cars functionality

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 30)

driver.get("https://phptravels.net/cars")


pickup = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='City or Airport']"))
)
pickup.click()
pickup.send_keys("Abu Dhabi")


pickup_option = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//div[@class='flex items-start gap-2'])[2]")
    )
)

pickup_option.click()



drop = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Same As Pick-up']"))
)
drop.click()
drop.clear()
drop.send_keys("Dubai")

drop_option = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//div[@class='font-medium text-sm'])[2]")
    )
)

drop_option.click()



pickup_date = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Pick-up Date']"))
)
pickup_date.click()

pickup_day = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//td[not(contains(@class,'disabled'))])[35]")
    )
)
pickup_day.click()



return_day = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//div[contains(text(),'31')])[2]")
    )
)
return_day.click()



search_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@type,'submit')]"))
)
search_btn.click()

wait.until(EC.url_contains("cars"))
print("Car search completed successfully!")

time.sleep(5)
driver.quit()
