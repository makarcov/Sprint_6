import allure

from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполняем поле Имя')
    def fill_name_field(self, locator, name):
        self.set_text(locator, name)

    @allure.step('Заполняем поле Фамилия')
    def fill_surname_field(self, locator, surname):
        self.set_text(locator, surname)

    @allure.step('Заполняем поле Адрес')
    def fill_address_field(self, locator, address):
        self.set_text(locator, address)

    @allure.step('Выбираем станцию метро')
    def choose_metro_station(self, locator_field, locator_dropdown):
        self.click_element(locator_field)
        self.click_element(locator_dropdown)

    @allure.step('Заполняем поле Телефон')
    def fill_phone_field(self, locator, phone):
        self.set_text(locator, phone)

    def fill_first_form(self, name_loc, name, surname_loc, surname, address_loc, address,
                        metro_field_loc, metro_dropdown_loc, phone_loc, phone):
        self.fill_name_field(name_loc, name)
        self.fill_surname_field(surname_loc, surname)
        self.fill_address_field(address_loc, address)
        self.choose_metro_station(metro_field_loc, metro_dropdown_loc)
        self.fill_phone_field(phone_loc, phone)

    @allure.step('Нажимаем кнопку Далее')
    def click_forward_button(self, locator):
        self.click_element(locator)

    @allure.step('Выбираем на календаре день начала аренды')
    def choose_start_day(self, calendar_field_loc, calendar_dropdown_loc):
        self.click_element(calendar_field_loc)
        self.click_element_with_js(calendar_dropdown_loc)

    @allure.step('Выбираем срок аренды')
    def choose_rental_period(self, days_field_loc, days_dropdown_loc):
        self.click_element(days_field_loc)
        self.click_element_with_js(days_dropdown_loc)

    @allure.step('Выбираем цвет скутера')
    def choose_scooter_colour(self, locator):
        self.click_element(locator)

    @allure.step('Заполняем поле Комментарий')
    def fill_comment_field(self, locator, comment):
        self.set_text(locator, comment)

    def fill_second_form(self, calendar_field_loc, calendar_dropdown_loc, days_field_loc, days_dropdown_loc,
                         scooter_colour_loc, comment_field_loc, comment):
        self.choose_start_day(calendar_field_loc, calendar_dropdown_loc)
        self.choose_rental_period(days_field_loc, days_dropdown_loc)
        self.choose_scooter_colour(scooter_colour_loc)
        self.fill_comment_field(comment_field_loc, comment)

    @allure.step('Нажимаем кнопку Заказать')
    def click_order_button(self, locator):
        self.click_element(locator)

    @allure.step('Нажимаем кнопку Да')
    def click_yes_button(self, locator):
        self.click_element(locator)

    @allure.step('Нажимаем кнопку Посмотреть статус')
    def click_view_status_button(self, locator):
        self.click_element(locator)
