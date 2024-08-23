import allure

from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_question(self, locator, number):
        locator = self.formated_locator(locator, number)
        return self.click_element(locator)

    @allure.step('Получение текста ответа')
    def get_answer(self, locator, number):
        locator = self.formated_locator(locator, number)
        return self.get_text(locator)

    def click_question_and_get_answer(self, locator_q, locator_a, number):
        self.click_question(locator_q, number)
        return self.get_answer(locator_a, number)


    @staticmethod
    @allure.step('Проверка соответсвия фактического текста ответа и ожидаемого')
    def check_answer(actual, expected):
        return actual == expected