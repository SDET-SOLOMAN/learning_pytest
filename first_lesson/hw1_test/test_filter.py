# Фильтр
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

FILTER = (By.XPATH, "//select[contains(@class, 'product_sort')]")
LOW_HIGH = (By.XPATH, "//span[@class='active_option']")
PRICES = (By.XPATH, "//div[@class='inventory_item_price']")
ITEM_NAMES = (By.XPATH, "//div[@class='inventory_item_name ']")


# Проверка работоспособности фильтра (low to high)
def test_filter_low_to_high(login):
    Select(login.find_element(*FILTER)).select_by_index(2)
    prices = login.find_elements(*PRICES)
    assert len(prices) == 6
    n = float(prices[0].text[1:])
    for num in prices:
        assert n <= float(num.text[1:]), f"Not filtered properly"
        n = float(num.text[1:])


# Проверка работоспособности фильтра (high to low)
def test_filter_high_to_low(login):
    Select(login.find_element(*FILTER)).select_by_index(3)
    prices = login.find_elements(*PRICES)
    assert len(prices) == 6
    n = float(prices[0].text[1:])
    for num in prices:
        assert n >= float(num.text[1:]), f"Not filtered properly"
        n = float(num.text[1:])


# Проверка работоспособности фильтра (A to Z)
def test_filter_a_to_z(login):
    Select(login.find_element(*FILTER)).select_by_index(0)
    items = login.find_elements(*ITEM_NAMES)
    list_items = [item.text.split() for item in items]
    items_order = [[ord(x[0]) for x in l] for l in list_items]
    previous = items_order[0]
    for item in items_order:
        ind = 0
        while len(item) < len(previous):
            item.append(0)
        while len(previous) < len(item):
            previous.append(0)
        for num in previous:
            if item[ind] < num and item[ind - 1] < previous[ind - 1]:
                assert 1 > 2, f"Not filtered properly {num}, {item[ind]} - {item[ind - 1]}"
            ind += 1
        previous = item


# Проверка работоспособности фильтра (Z to A)
def test_filter_z_to_a(login):
    Select(login.find_element(*FILTER)).select_by_index(1)
    items = login.find_elements(*ITEM_NAMES)
    list_items = [item.text.split() for item in items]
    items_order = [[ord(x[0]) for x in l] for l in list_items]
    previous = items_order[0]
    for item in items_order:
        ind = 0
        while len(item) < len(previous):
            item.append(0)
        while len(previous) < len(item):
            previous.append(0)
        for num in previous:
            if item[ind] > num and item[ind - 1] > previous[ind - 1]:
                assert 1 > 2, f"Not filtered properly {num}, {item[ind]} - {item[ind - 1]}"
            ind += 1
        previous = item
