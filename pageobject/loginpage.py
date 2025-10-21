from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.signup_header = (By.XPATH, "//h2[text()='New User Signup!']")
        self.username = (By.NAME, "name")
        self.email_signup = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
        self.signup_button = (By.XPATH, "//button[text()='Signup']")
        self.email_login = (By.CSS_SELECTOR, "input[data-qa = 'login-email']")
        self.password = (By.CSS_SELECTOR, "input[data-qa = 'login-password']")
        self.login_button = (By.CSS_SELECTOR, "button[data-qa = 'login-button']")

    def signup(self, username, email):
        assert self.driver.find_element(*self.signup_header).is_displayed()
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.email_signup).send_keys(email)
        self.driver.find_element(*self.signup_button).click()

    def login(self, email, password):
        self.driver.find_element(*self.email_login).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()
