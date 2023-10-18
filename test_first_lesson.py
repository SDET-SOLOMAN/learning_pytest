from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

BASE_URL = "https://www.saucedemo.com/"
STANDARD_USER = "standard_user"
STANDARD_PASS = "secret_sauce"
USER_NAME_FIELD = "//input[contains(@class, 'input_error') and @id='user-name']"
PASS_FIELD = "//input[contains(@class, 'input_error') and @id='password']"
LOGIN_BUTTON = "//input[@id='login-button']"


def test_happy_flow():
    driver.get(BASE_URL)

    user_name_field = driver.find_element(By.XPATH, USER_NAME_FIELD)
    user_name_field.send_keys(STANDARD_USER)

    password = driver.find_element(By.XPATH, PASS_FIELD)
    password.send_keys(STANDARD_PASS)

    login = driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    driver.quit()
