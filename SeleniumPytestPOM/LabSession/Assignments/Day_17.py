#  Write an automation script to search selenium in google search for auto suggestion
# functionality. Pick the auto suggested text and verify if the web site is redirected.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ------------------ DRIVER SETUP ------------------

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# ------------------ STEP 1 : OPEN GOOGLE ------------------

driver.get("https://www.google.com")

search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
search_box.send_keys("selenium")

# ------------------ STEP 2 : HANDLE AUTO SUGGESTION ------------------

suggestions = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li"))
)

print("Auto Suggestions Found:")

first_suggestion = None

for suggestion in suggestions:
    text = suggestion.text
    if text != "":
        print(text)
        first_suggestion = suggestion
        break

first_suggestion.click()

# ------------------ STEP 3 : VERIFY REDIRECTION ------------------

wait.until(EC.title_contains("selenium"))

if "selenium" in driver.title.lower():
    print("✅ Successfully redirected after selecting auto suggestion")
else:
    print("❌ Redirection failed")


print("Main Page Title:", driver.title)
sho_more = wait.until(EC.element_to_be_clickable((By.XPATH,"(//div//span[contains(text(),'Show more')])[1]")))
#sho_more.click()
driver.execute_script("arguments[0].scrollIntoView({block:'center'});", sho_more)

time.sleep(1)

driver.execute_script("arguments[0].click();", sho_more)

time.sleep(3)

driver.quit()

