# Добавление товара в корзину через каталог
# Удаление товара из корзины через корзину
# Добавление товара в корзину из карточки товара
# Удаление товара из корзины через карточку товара
import pytest
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://www.saucedemo.com/"
STANDARD_USER = "standard_user"
STANDARD_PASS = "secret_sauce"
USER_NAME = (By.XPATH, "//form // input[@placeholder='Username']")
USER_PASS = (By.XPATH, "//input[contains(@type, 'passw')]")
LOGIN = (By.XPATH, "//input[@data-test='login-button']")
NEEDED_URL = 'inventory'
LOGO_TEXT = "Swag Labs"
LOGO_TEXT_ACTUAL = (By.XPATH, "//div[@class='app_logo' and text()='Swag Labs']")
ACTUAL_ERROR = (By.XPATH, "//h3[@data-test='error']")
BABY_ITEM = (By.XPATH, "//a[@id='item_2_title_link']")
ITEMS = (By.XPATH, "//div[@class='pricebar']//button[contains(@id, 'add-to-cart')]")
REMOVE = (By.XPATH, "//button[@id='remove-sauce-labs-onesie']")
SHOPPING_CART = (By.XPATH, "//a[@class='shopping_cart_link'] / span")
CHECK_OUT = (By.XPATH, "//div[@class='cart_footer']//button[@name='checkout']")
ACTUAL_CHECKOUT_TEXT = (By.XPATH, "//div[@id='header_container']//span[@class='title']")
EXPECTED_CHECKOUT = "Checkout: Your Information"
NAME = "Sheikh el Hassan Del Hussain"
NAME_FIELD = (By.XPATH, "//div[@class='form_group']/input[@name='firstName']")
LAST = "Gonzales el Loko della Sollo"
LAST_FIELD = (By.XPATH, "//div[@class='form_group']/input[@name='lastName']")
ZIP = 66666
ZIP_FIELD = (By.XPATH, "//div[@class='form_group']/input[@name='postalCode']")

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


# Добавление товара в корзину через каталог
def test_add_item_through_catalog(login):
    items = login.find_elements(*ITEMS)
    for i, c in enumerate(items):
        if i == 4:
            c.click()
            wait = WebDriverWait(login, 10)
            remove = wait.until(EC.presence_of_element_located(REMOVE)).text
            print(remove)
            assert "Remove" == remove, f"Expected Text: Remove not found, found actual: {remove}"
    added_item_name = login.find_element(*BABY_ITEM).text
    shopping = login.find_element(*SHOPPING_CART)
    assert 1 == int(shopping.text), f"Shopping cart is not equal to 1"
    shopping.click()
    actual_item_name = login.find_element(*BABY_ITEM).text
    print(added_item_name, actual_item_name)
    sleep(2)
    assert actual_item_name == added_item_name, f"Items don't match"
    login.find_element(*CHECK_OUT).click()
    actual_check = login.find_element(*ACTUAL_CHECKOUT_TEXT).text
    assert EXPECTED_CHECKOUT == actual_check
    login.find_element(*NAME_FIELD).send_keys(NAME)
    login.find_element(*LAST_FIELD).send_keys(LAST)
    login.find_element(*ZIP_FIELD).send_keys(ZIP)





    # Оформление заказа используя корректные данные

    # Удаление товара из корзины через корзину