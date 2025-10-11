from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.login_link = (By.CSS_SELECTOR, "a[href='/login']")
        self.title = "Automation Exercise"

    def homepage_validation(self):
        assert self.driver.title == self.title
        self.driver.find_element(*self.login_link).click()

