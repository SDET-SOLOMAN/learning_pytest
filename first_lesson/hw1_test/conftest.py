import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://www.saucedemo.com/"
STANDARD_USER = "standard_user"
STANDARD_PASS = "secret_sauce"
USER_NAME = (By.XPATH, "//form // input[@placeholder='Username']")
USER_PASS = (By.XPATH, "//input[contains(@type, 'passw')]")
LOGIN = (By.XPATH, "//input[@data-test='login-button']")
NEEDED_URL = 'inventory'
LOGO_TEXT = "Swag Labs"
LOGO_TEXT_ACTUAL = (By.XPATH, "//div[@class='app_logo' and text()='Swag Labs']")

@pytest.fixture(scope='session')
def driver():
    print('\nstart browser...')
    chrome_options = Options()
    if 'CI' in os.environ:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.maximize_window()
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
    yield driver
    print('\nquit browser...')
    driver.quit()

@pytest.fixture(scope='session')
def login(driver):
    driver.get(BASE_URL)
    driver.find_element(*USER_NAME).send_keys(STANDARD_USER)
    driver.find_element(*USER_PASS).send_keys(STANDARD_PASS)
    driver.find_element(*LOGIN).click()
    assert NEEDED_URL in driver.current_url, f"{NEEDED_URL} is missing from the url"
    text = driver.find_element(*LOGO_TEXT_ACTUAL).text
    assert LOGO_TEXT == text, f"Expected text: {LOGO_TEXT} is not equal to actual: {LOGO_TEXT_ACTUAL}"
    yield driver



# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options as OptionsFirefox
# import time
#
# supported_browsers = {
#     'chrome': webdriver.Chrome,
#     'firefox': webdriver.Firefox
# }


# @pytest.fixture(scope="session")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     user_language = request.config.getoption("language")
#
#     options = Options()
#     options.add_experimental_option(
#         'prefs', {'intl.accept_languages': user_language})
#
#     options_firefox = OptionsFirefox()
#     options_firefox.set_preference("intl.accept_languages", user_language)
#
#     browser = None
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         browser = webdriver.Chrome(options=options)
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox(options=options_firefox)
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
