from selenium.webdriver.common.by import By


class RegisterForm:
    def __init__(self, driver):
        self.driver = driver
        self.header = (By.XPATH, "//h2/b[text()='Enter Account Information']")
        self.gender = (By.ID, "id_gender1")
        self.password = (By.ID, "password")
        self.day = (By.ID, "days")
        self.month = (By.ID,"months")
        self.year = (By.CSS_SELECTOR, "#years")
        self.newsletter = (By.ID, "newsletter")
        self.option = (By.ID, "optin")
        self.first_name = (By.ID, "first_name")
        self.last_name = (By.ID, "last_name")
        self.company = (By.ID, "company")
        self.address1 = (By.ID, "address1")
        self.address2 = (By.ID, "address2")
        self.country = (By.ID, "country")
        self.state = (By.ID, "state")
        self.city = (By.ID, "city")
        self.zipcode = (By.ID, "zipcode")
        self.telephone = (By.ID, "mobile_number")
        self.button = (By.XPATH, "//button[text()='Create Account']")

    def register_form(self, password, day, month, year, first_name, last_name,
                      company_name, adderss1, adderss2, country, state, city, zipcode, telephone):

        assert self.driver.find_element(*self.header).is_displayed()
        self.driver.find_element(*self.gender).click()
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.day).send_keys(day)
        self.driver.find_element(*self.month).send_keys(month)
        self.driver.find_element(*self.year).send_keys(year)
        self.driver.find_element(*self.newsletter).click()
        self.driver.find_element(*self.option).click()
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.company).send_keys(company_name)
        self.driver.find_element(*self.address1).send_keys(adderss1)
        self.driver.find_element(*self.address2).send_keys(adderss2)
        self.driver.find_element(*self.country).send_keys(country)
        self.driver.find_element(*self.state).send_keys(state)
        self.driver.find_element(*self.city).send_keys(city)
        self.driver.find_element(*self.zipcode).send_keys(zipcode)
        self.driver.find_element(*self.telephone).send_keys(telephone)
        self.driver.find_element(*self.button).click()