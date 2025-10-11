import json

import pytest
from selenium.webdriver.common.by import By

from pageobject.homepage import HomePage
from pageobject.loginpage import LoginPage
from pageobject.register_form import RegisterForm

data_path = 'Data/data.json'
with open(data_path) as f:
    data = json.load(f)
    users = data['users']

@pytest.mark.parametrize("user", users)
def test_registration(BrowserInstance, user):

    driver = BrowserInstance
    homepage = HomePage(driver)
    homepage.homepage_validation()
    login_page = LoginPage(driver)
    login_page.signup(user['username'], user['email'])
    register_form = RegisterForm(driver)
    register_form.register_form(user['password'], user['day'], user['month'], user['year'],
                                user['first_name'], user['last_name'], user['company_name'],
                                user['address1'], user['address2'], user['country'],user['state'],
                                user['city'], user['zipcode'], user['telephone'])



    assert driver.find_element(By.XPATH,"//b[text()='Account Created!']").is_displayed()
    print("Account Created")
    driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']").click()
    assert driver.find_element(By.XPATH,"//a[text()=' Logged in as ']").is_displayed()
    print("Logged in")
    username = user['username']
    assert driver.find_element(By.XPATH,f"//b[text()='{username}']").is_displayed()
    driver.find_element(By.CSS_SELECTOR, "a[href='/delete_account']").click()
    assert driver.find_element(By.XPATH,"//b[text()='Account Deleted!']").is_displayed()
    print("Account Deleted")
    driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']").click()
