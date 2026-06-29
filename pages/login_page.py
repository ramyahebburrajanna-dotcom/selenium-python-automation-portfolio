from selenium.webdriver.common.by import By

class LoginPage:

    # Locators
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, user):
        self.driver.find_element(*self.username).send_keys(user)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, user, pwd):
        self.enter_username(user)
        self.enter_password(pwd)
        self.click_login()