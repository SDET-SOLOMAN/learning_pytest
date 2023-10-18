from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Авторизация using XPATH ONLY
BASE_URL = "https://www.saucedemo.com/"
STANDARD_USER = "standard_user"
STANDARD_PASS = "secret_sauce"
NEGATIVE_USER = 'user'
NEGATIVE_PASS = 'user'
USER_NAME = (By.XPATH, "//form // input[@placeholder='Username']")
USER_PASS = (By.XPATH, "//input[contains(@type, 'passw')]")
LOGIN = (By.XPATH, "//input[@data-test='login-button']")
NEEDED_URL = 'inventory'
LOGO_TEXT = "Swag Labs"
LOGO_TEXT_ACTUAL = (By.XPATH, "//div[@class='app_logo' and text()='Swag Labs']")
ERROR_MESSAGE = "Epic sadface: Username and password do not match any user in this service"
ACTUAL_ERROR = (By.XPATH, "//h3[@data-test='error']")

# Авторизация используя корректные данные (standard_user, secret_sauce)
def test_positive_flow(driver):
    driver.get(BASE_URL)
    driver.find_element(*USER_NAME).send_keys(STANDARD_USER)
    driver.find_element(*USER_PASS).send_keys(STANDARD_PASS)
    driver.find_element(*LOGIN).click()
    assert NEEDED_URL in driver.current_url, f"{NEEDED_URL} is missing from the url"
    text = driver.find_element(*LOGO_TEXT_ACTUAL).text
    assert LOGO_TEXT == text, f"Expected text: {LOGO_TEXT} is not equal to actual: {LOGO_TEXT_ACTUAL}"


# Авторизация используя некорректные данные (user, user)
def test_negative_flow(driver):
    driver.get(BASE_URL)
    driver.find_element(*USER_NAME).send_keys(NEGATIVE_USER)
    driver.find_element(*USER_PASS).send_keys(NEGATIVE_PASS)
    driver.find_element(*LOGIN).click()
    wait = WebDriverWait(driver, 10)
    actual = wait.until(EC.presence_of_element_located(ACTUAL_ERROR))
    print(actual.text)
    assert ERROR_MESSAGE == actual.text
    # assert NEEDED_URL in driver.current_url, f"{NEEDED_URL} is missing from the url"
    # text = driver.find_element(*LOGO_TEXT_ACTUAL).text
    # assert LOGO_TEXT == text, f"Expected text: {LOGO_TEXT} is not equal to actual: {LOGO_TEXT_ACTUAL}"
