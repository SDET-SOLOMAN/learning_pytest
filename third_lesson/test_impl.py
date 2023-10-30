import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


MAIN_PAGE = "https://victoretc.github.io/selenium_waits/"
LOGIN = "login"
PASSWORD = "password"
START_BUTTON = "//button[@id='startTest']"
LOGIN_FIELD = "login"
PASSWORD_FIELD = "password"
REGISTER_BUTTON = "register"
CHECKBOX = "agree"
SUCCESS_MESSAGE = "successMessage"
LOADER = "loader"


def test_registration_implicit(driver):

    driver.get(MAIN_PAGE)
    header = driver.find_element(By.XPATH, '//h1')
    assert header.text == "Практика с ожиданиями в Selenium"

    start_button = driver.find_element(By.XPATH, START_BUTTON)
    assert start_button.is_displayed() or start_button.is_enabled()  # Check for visibility or enablement
    start_button.click()

    login_field = driver.find_element(By.ID, LOGIN_FIELD)
    login_field.send_keys(LOGIN)

    password_field = driver.find_element(By.ID, PASSWORD_FIELD)
    password_field.send_keys(PASSWORD)

    checkbox_field = driver.find_element(By.ID, CHECKBOX)
    checkbox_field.click()

    register_button = driver.find_element(By.ID, REGISTER_BUTTON)
    register_button.click()

    time.sleep(1)

    loader_button = driver.find_element(By.ID, LOADER)
    print(loader_button.is_displayed())

    time.sleep(4)

    success_message = driver.find_element(By.ID, SUCCESS_MESSAGE)
    assert success_message.text == "Вы успешно зарегистрированы!"