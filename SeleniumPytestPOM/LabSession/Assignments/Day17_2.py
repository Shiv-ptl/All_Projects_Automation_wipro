# 2. Write an automation script in selenium python to search flights in make my
# trip.com and validate that the user is on the correct redirected page




from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

#
# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--disable-popup-blocking")

driver:WebDriver = webdriver.Firefox()

# driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 25)

driver.get("https://www.makemytrip.com/")



try:
    close_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='commonModal__close']"))
    )
    close_button.click()
except TimeoutException:
    pass


driver.find_element(By.TAG_NAME, "body").click()


driver.find_element(By.XPATH, "//img[@alt='minimize']").click()


from_city = wait.until(
    EC.element_to_be_clickable((By.ID, "fromCity"))
)
driver.execute_script("arguments[0].click();", from_city)

driver.find_element(By.TAG_NAME, "body").click()


driver.find_element(By.XPATH, "//img[@alt='minimize']").click()

from_input = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='From']"))
)
from_input.send_keys("Delhi")
time.sleep(2)
from_input.send_keys(Keys.ARROW_DOWN)
from_input.send_keys(Keys.ENTER)



to_city = wait.until(
    EC.element_to_be_clickable((By.ID, "toCity"))
)
driver.execute_script("arguments[0].click();", to_city)

to_input = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='To']"))
)
to_input.send_keys("Mumbai")
time.sleep(2)
to_input.send_keys(Keys.ARROW_DOWN)
to_input.send_keys(Keys.ENTER)



departure_date = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@aria-label and not(contains(@class,'disabled'))]")
    )
)
departure_date.click()



search_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Search']"))
)
search_button.click()



wait.until(EC.url_contains("flight/search"))

current_url = driver.current_url

if "flight/search" in current_url:
    print("User successfully redirected to Flights Search Results page.")
else:
    print("Redirection failed.")


# Wait to see result
time.sleep(5)

driver.quit()