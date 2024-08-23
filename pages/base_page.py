from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # переход по заданному адресу
    def get_url(self, url):
        return self.driver.get(url)

    # найти элемент с использованием ожидания
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # найти кликабельный элемент с использованием ожидания
    def find_element_to_click_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    # кликнуть по элементу
    def click_element(self, locator):
        element = self.find_element_to_click_with_wait(locator)
        return element.click()

    # получить текст элемента
    def get_text(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    # ввести текст в элемент
    def set_text(self, locator, text):
        element = self.find_element_with_wait(locator)
        return element.send_keys(text)

    # скролл до элемента
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # кликнуть на элемент с использованием JavaScript
    def click_element_with_js(self, locator):
        element = self.find_element_to_click_with_wait(locator)
        return self.driver.execute_script("arguments[0].click();", element)

    # отформатировать локатор общего вида
    def formated_locator(self, locator, number):
        method, locator = locator
        locator = locator.format(number)
        return [method, locator]

    # получить url текущей страницы
    def get_current_url(self):
        return self.driver.current_url

    # переключиться на окно Дзена
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains('https://dzen.ru/'))
