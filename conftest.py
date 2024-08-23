import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import URL
from helpers import Helpers
from locators.main_page_locators import MainPageLocators


# запуск драйвера
@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


# драйвер, запускающий главную страницу
@pytest.fixture()
def driver_main_page(driver):
    driver.get(URL.main_page_url)
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.POPUP_WINDOW))
    driver.find_element(*MainPageLocators.POPUP_WINDOW).click()
    yield driver
    driver.quit()

@pytest.fixture()
def name():
    return Helpers.generate_name()

@pytest.fixture()
def surname():
    return Helpers.generate_surname()

@pytest.fixture()
def address():
    return Helpers.generate_address()

@pytest.fixture()
def metro_station_number():
    return Helpers.generate_number_for_metro_station()

@pytest.fixture()
def phone():
    return Helpers.generate_phone_number()
