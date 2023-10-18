from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"
MAIN_PAGE = "https://www.saucedemo.com/inventory.html"
USER_FILD = (By.ID, "user-name")
PASSWORD_FILD = (By.ID, "password")
LOGIN_BTN = (By.ID, "login-button")
ERROR_MES = (By.CSS_SELECTOR, ".error-message-container.error")
ERROR_TXT = 'Epic sadface: Username and password do not match any user in this service'

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get(BASE_URL)



# def test_login_form():
#     driver.get("https://www.saucedemo.com/")
#
#     username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
#     username_field.send_keys("standard_user")
#
#     password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
#     password_field.send_keys("secret_sauce")
#
#     login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
#     login_button.click()
#
#     time.sleep(5)
#     assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    # driver.quit()

@pytest.fixture(scope='function')
def log_in(driver):
    driver.get(BASE_URL)
    user_fild = driver.find_element(*USER_FILD)
    pass_fild = driver.find_element(*PASSWORD_FILD)
    user_fild.send_keys("standard_user")
    pass_fild.send_keys("secret_sauce")
    driver.find_element(*LOGIN_BTN).click()
    yield driver.current_url


def test_login_form(log_in, driver):
    driver.get(BASE_URL)
    # time.sleep(1)
    assert log_in == MAIN_PAGE, f'expected result {MAIN_PAGE}, but got {log_in} '


def test_wrong_Login(driver):
    driver.get(BASE_URL)
    user_fild2 = driver.find_element(*USER_FILD)
    pass_fild2 = driver.find_element(*PASSWORD_FILD)
    user_fild2.send_keys("user")
    pass_fild2.send_keys("user")
    driver.find_element(*LOGIN_BTN).click()

    error = driver.find_element(*ERROR_MES).text
    assert error == ERROR_TXT, f'expected result {ERROR_TXT}, but got {error} '