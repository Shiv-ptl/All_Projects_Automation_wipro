import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager


class Test_Dropdown:

    def test_dropdown(self):

        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get('https://trytestingthis.netlify.app/')

        time.sleep(3)

        # -------- Single Select --------
        dropdown = driver.find_element(By.ID, "option")
        sel = Select(dropdown)

        sel.select_by_visible_text("Option 1")
        time.sleep(1)

        sel.select_by_value("option 2")
        time.sleep(1)

        sel.select_by_index(3)
        time.sleep(2)

        checkbox_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

        print("Total checkboxes:", len(checkbox_list))

        for checkbox in checkbox_list:
            checkbox.click()
            time.sleep(1)


        for checkbox in checkbox_list:
            if checkbox.is_selected():
                checkbox.click()
                time.sleep(1)

        multi_sel_element = driver.find_element(By.ID, "owc")

        multi_sel = Select(multi_sel_element)

        multi_sel.select_by_visible_text("Option 1")
        time.sleep(1)

        multi_sel.select_by_visible_text("Option 2")
        time.sleep(1)

        multi_sel.select_by_visible_text("Option 3")
        time.sleep(2)
        multi_sel.deselect_by_visible_text("Option 2")
        time.sleep(2)

        multi_sel.deselect_all()
        time.sleep(2)

        # sel = Select(driver.find_element(By.ID, "owc"))
        #
        # for option in sel.options:
        #     print(option.text, option.is_selected())


        driver.quit()
