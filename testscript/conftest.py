import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", choices=["chrome", "firefox"], help="browser to use"
    )

@pytest.fixture(scope='function')
def BrowserInstance(request):
    browser = request.config.getoption('browser')
    if browser == 'chrome':
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "profile.password_manager_leak_detection": False,
        })
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == 'firefox':
        driver = webdriver.Firefox()

    driver.get('http://automationexercise.com')
    driver.implicitly_wait(5)
    yield driver
    driver.quit()