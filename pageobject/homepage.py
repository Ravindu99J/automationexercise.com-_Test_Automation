from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver,username):
        self.driver = driver
        self.login_link_locator = (By.CSS_SELECTOR, "a[href='/login']")
        self.title = "Automation Exercise"
        self.login_as = (By.XPATH, "//a[text()=' Logged in as ']")
        self.username = (By.XPATH, f"//b[text()='{username}']")
        self.delete_link = (By.CSS_SELECTOR, "a[href='/delete_account']")
        self.delete_message = (By.XPATH, "//b[text()='Account Deleted!']")
        self.continue_button = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
        self.logout_button = (By.XPATH, '//a[text()= " Logout"]')

    def homepage_validation(self):
        assert self.driver.title == self.title

    def login_link(self):
        self.driver.find_element(*self.login_link_locator).click()

    def validate_login(self):
        assert self.driver.find_element(*self.login_as).is_displayed()
        assert self.driver.find_element(*self.username).is_displayed()
        print("Login Successful")

    def delete_account(self):
        self.driver.find_element(*self.delete_link).click()
        assert self.driver.find_element(*self.delete_message).is_displayed()
        print("Account Deleted")
        self.driver.find_element(*self.continue_button).click()

    def logout(self):
        self.driver.find_element(*self.logout_button).click()