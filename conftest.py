import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


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
