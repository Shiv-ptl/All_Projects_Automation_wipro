# 2. Write an automation script to sign up as a agent in php travels website
# https://phptravels.net/signup?type=agent
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -------- Setup --------
driver:WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 25)

driver.get("https://phptravels.net/signup?type=agent")
time.sleep(5)

# -------- Fill Form --------
wait.until(EC.visibility_of_element_located((By.NAME, "first_name"))).send_keys("shiv")
driver.find_element(By.NAME, "last_name").send_keys("ptl")
driver.find_element(By.NAME, "email").send_keys("shiv12345ptl@gmail.com")
driver.find_element(By.NAME, "password").send_keys("Test@1234")
wait.until(
    EC.visibility_of_element_located((By.ID, "confirm_password"))
).send_keys("Test@1234")

# -------- Handle Security Question --------
# -------- Handle Security Question --------
question_element = wait.until(
    EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Security')]"))
)

question_text = question_element.text.lower()
print("Security Question:", question_text)

words_to_numbers = {
    "zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,
    "six":6,"seven":7,"eight":8,"nine":9,"ten":10,
    "eleven":11,"twelve":12,"thirteen":13,"fourteen":14,
    "fifteen":15,"sixteen":16,"seventeen":17,
    "eighteen":18,"nineteen":19,"twenty":20
}

# Clean text
clean_text = question_text.replace("?", "").replace("*", "")

words = clean_text.split()

numbers = []
operator = None

for word in words:
    if word in words_to_numbers:
        numbers.append(words_to_numbers[word])
    elif word in ["plus", "minus", "times", "multiplied", "divided"]:
        operator = word

if len(numbers) == 2 and operator:
    num1, num2 = numbers

    if operator == "plus":
        answer = num1 + num2
    elif operator == "minus":
        answer = num1 - num2
    elif operator in ["times", "multiplied"]:
        answer = num1 * num2
    elif operator == "divided":
        answer = num1 // num2   # integer division

else:
    raise Exception("Could not parse security question properly.")

print("Calculated Answer:", answer)

driver.find_element(By.ID, "captcha_answer").send_keys(str(answer))
driver.find_element(By.XPATH,"//div[@class='checkbox-custom']").click()

# -------- Submit --------
signup_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
signup_btn.click()
time.sleep(5)
print("Agent signup form submitted successfully!")

time.sleep(5)
driver.quit()
