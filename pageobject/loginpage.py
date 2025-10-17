from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.signup_header = (By.XPATH, "//h2[text()='New User Signup!']")
        self.username = (By.NAME, "name")
        self.email = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
        self.signup_button = (By.XPATH, "//button[text()='Signup']")

    def signup(self, username, email):
        assert self.driver.find_element(*self.signup_header).is_displayed()
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.signup_button).click()
