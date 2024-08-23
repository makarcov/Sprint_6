import pytest
import allure

from locators.order_page_locators import OrderPageLocators
from locators.header_footer_locators import HeaderLocators, FooterLocators
from data import Comments
from data import URL
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка заказа самоката')
    @allure.description('Проверяем позитивный сценарий с двумя наборами данных. Проверяем две точки входа в сценарий: кнопка «Заказать» вверху страницы и внизу.')
    @pytest.mark.parametrize('order_button', [HeaderLocators.ORDER_BUTTON_HEADER, FooterLocators.ORDER_BUTTON_FOOTER])
    def test_order_with_upper_button_success(self, driver_main_page, order_button, name, surname, address, phone):
        order_page = OrderPage(driver_main_page)
        order_page.click_element(order_button)
        order_page.fill_first_form(OrderPageLocators.NAME_FIELD, name,
                                   OrderPageLocators.SURNAME_FIELD, surname,
                                   OrderPageLocators.ADDRESS_FIELD, address,
                                   OrderPageLocators.METRO_STATION_FIELD, OrderPageLocators.METRO_STATION,
                                   OrderPageLocators.PHONE_FIELD, phone
                                   )
        order_page.click_forward_button(OrderPageLocators.FORWARD_BUTTON)
        order_page.fill_second_form(OrderPageLocators.CALENDAR_FIELD, OrderPageLocators.CALENDAR_CHOOSE_NEXT_DAY_DROPDOWN,
                                    OrderPageLocators.DAYS_PERIOD_FIELD, OrderPageLocators.DAYS_PERIOD_CHOOSE_DROPDOWN_LIST,
                                    OrderPageLocators.SCOOTER_COLOR_BLACK_CHECKBOX,
                                    OrderPageLocators.COMMENT_FIELD, Comments.COMMENT_1
                                    )
        order_page.click_order_button(OrderPageLocators.ORDER_BUTTON)
        order_page.click_yes_button(OrderPageLocators.YES_BUTTON)
        assert order_page.find_element_with_wait(OrderPageLocators.VIEW_STATUS_BUTTON).is_displayed()

    @allure.title('Проверка переход по клику на лого «Самокат»')
    @allure.description('Если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    @pytest.mark.parametrize('order_button', [HeaderLocators.ORDER_BUTTON_HEADER, FooterLocators.ORDER_BUTTON_FOOTER])
    def test_upper_button_click_on_scooter_logo_success(self, driver_main_page, order_button, name, surname, address, phone):
        order_page = OrderPage(driver_main_page)
        order_page.click_element(order_button)
        order_page.fill_first_form(OrderPageLocators.NAME_FIELD, name,
                                   OrderPageLocators.SURNAME_FIELD, surname,
                                   OrderPageLocators.ADDRESS_FIELD, address,
                                   OrderPageLocators.METRO_STATION_FIELD, OrderPageLocators.METRO_STATION,
                                   OrderPageLocators.PHONE_FIELD, phone
                                   )
        order_page.click_forward_button(OrderPageLocators.FORWARD_BUTTON)
        order_page.fill_second_form(OrderPageLocators.CALENDAR_FIELD,
                                    OrderPageLocators.CALENDAR_CHOOSE_NEXT_DAY_DROPDOWN,
                                    OrderPageLocators.DAYS_PERIOD_FIELD,
                                    OrderPageLocators.DAYS_PERIOD_CHOOSE_DROPDOWN_LIST,
                                    OrderPageLocators.SCOOTER_COLOR_BLACK_CHECKBOX,
                                    OrderPageLocators.COMMENT_FIELD, Comments.COMMENT_1
                                    )
        order_page.click_order_button(OrderPageLocators.ORDER_BUTTON)
        order_page.click_yes_button(OrderPageLocators.YES_BUTTON)
        order_page.click_view_status_button(OrderPageLocators.VIEW_STATUS_BUTTON)
        order_page.click_element(HeaderLocators.SCOOTER_LOGO)
        assert order_page.get_current_url() == URL.main_page_url

    @allure.title('Проверка переход по клику на лого «Яндекс»')
    @allure.description('Если нажать на логотип «Яндекса», в новом окне через редирект откроется главная страница Дзена.')
    @pytest.mark.parametrize('order_button', [HeaderLocators.ORDER_BUTTON_HEADER, FooterLocators.ORDER_BUTTON_FOOTER])
    def test_upper_button_click_on_yandex_logo_success(self, driver_main_page, order_button, name, surname, address, phone):
        order_page = OrderPage(driver_main_page)
        order_page.click_element(order_button)
        order_page.fill_first_form(OrderPageLocators.NAME_FIELD, name,
                                   OrderPageLocators.SURNAME_FIELD, surname,
                                   OrderPageLocators.ADDRESS_FIELD, address,
                                   OrderPageLocators.METRO_STATION_FIELD, OrderPageLocators.METRO_STATION,
                                   OrderPageLocators.PHONE_FIELD, phone
                                   )
        order_page.click_forward_button(OrderPageLocators.FORWARD_BUTTON)
        order_page.fill_second_form(OrderPageLocators.CALENDAR_FIELD,
                                    OrderPageLocators.CALENDAR_CHOOSE_NEXT_DAY_DROPDOWN,
                                    OrderPageLocators.DAYS_PERIOD_FIELD,
                                    OrderPageLocators.DAYS_PERIOD_CHOOSE_DROPDOWN_LIST,
                                    OrderPageLocators.SCOOTER_COLOR_BLACK_CHECKBOX,
                                    OrderPageLocators.COMMENT_FIELD, Comments.COMMENT_1
                                    )
        order_page.click_order_button(OrderPageLocators.ORDER_BUTTON)
        order_page.click_yes_button(OrderPageLocators.YES_BUTTON)
        order_page.click_view_status_button(OrderPageLocators.VIEW_STATUS_BUTTON)
        order_page.click_element(HeaderLocators.YANDEX_LOGO)
        order_page.switch_to_new_window()
        assert order_page.get_current_url() == URL.dzen_url
