from selenium.webdriver.common.by import By


class LoginPage:
    #locators
    username_input = (By.NAME,"username")
    password_input = (By.NAME,"password")
    login_button = (By.XPATH,"//button[@type='submit']")
    dashboard_text = (By.XPATH,"//h6[normalize-space()='Dashboard']")


    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(self.password_input).send_keys(password)

    #click on login button
        # click login button
        def click_login(self):
            self.driver.find_element(*self.login_button).click()

        # combined login action
        def logon(self, username, password):
            self.enter_username(username)
            self.enter_password(password)
            self.click_login()

        # verify dashboard
        def is_dashboard_visible(self):
            return self.driver.find_element(*self.dashboard_text).is_displayed()

