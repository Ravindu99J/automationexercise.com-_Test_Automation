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
    username = user['username']
    homepage = HomePage(driver,username)
    homepage.homepage_validation()
    login_page = LoginPage(driver)
    login_page.signup(user['username'], user['email'])
    register_form = RegisterForm(driver)
    register_form.register_form(user['password'], user['day'], user['month'], user['year'],
                                user['first_name'], user['last_name'], user['company_name'],
                                user['address1'], user['address2'], user['country'],user['state'],
                                user['city'], user['zipcode'], user['telephone'])


    homepage.validate_login()
    homepage.delete_account()
