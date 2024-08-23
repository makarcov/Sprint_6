import pytest
import allure

from data import Answers
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка теста ответов на вопросы')
    @allure.description('Проверяем выпадающий список в разделе «Вопросы о важном». Нужно проверить, что при нажатии на стрелочку, открывается соответствующий текст.')
    @pytest.mark.parametrize('question_numbers, expected_answers',
                             [
                                 (0, Answers.ANSWER_1),
                                 (1, Answers.ANSWER_2),
                                 (2, Answers.ANSWER_3),
                                 (3, Answers.ANSWER_4),
                                 (4, Answers.ANSWER_5),
                                 (5, Answers.ANSWER_6),
                                 (6, Answers.ANSWER_7),
                                 (7, Answers.ANSWER_8)
                             ])
    def test_answers_success(self, driver_main_page, question_numbers, expected_answers):
        main_page = MainPage(driver_main_page)
        actual_result = main_page.click_question_and_get_answer(
            MainPageLocators.QUESTIONS_COMMON, MainPageLocators.ANSWERS_COMMON, question_numbers)
        assert main_page.check_answer(actual_result, expected_answers)
