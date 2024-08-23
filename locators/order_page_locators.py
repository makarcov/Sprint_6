from selenium.webdriver.common.by import By


class OrderPageLocators:

    # локаторы первой формы заказа
    NAME_FIELD = [By.XPATH, '//input[@placeholder="* Имя"]']  # поле Имя
    SURNAME_FIELD = [By.XPATH, '//input[@placeholder="* Фамилия"]']  # поле Фамилия
    ADDRESS_FIELD = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']  # поле Адрес
    METRO_STATION_FIELD = [By.XPATH, '//input[@placeholder="* Станция метро"]']  # поле Метро
    METRO_STATION = [By.XPATH, '//*[text()="Бульвар Рокоссовского"]']  # выпадающий список станций метро
    # METRO_STATION_CHOOSE_DROPDOWN_LIST = [By.XPATH, 'li[@class="select-search__row"]/button[@value={}]']
    PHONE_FIELD = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']  # поле Телефон

    FORWARD_BUTTON = [By.XPATH, '//button[text()="Далее"]']  # кнопка Далее

    # локаторы второй формы заказа
    CALENDAR_FIELD = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']  # поле Дата
    CALENDAR_CHOOSE_NEXT_DAY_DROPDOWN = [By.XPATH, '//div[contains(@class,"today")]/following-sibling::div[1]']  # завтрашний день на календаре
    DAYS_PERIOD_FIELD = [By.XPATH, '//div[text()="* Срок аренды"]']  # поле Срок аренды
    DAYS_PERIOD_CHOOSE_DROPDOWN_LIST = [By.XPATH, '//div[text()="трое суток"]']  # выпадающий список количества дней аренды
    SCOOTER_COLOR_BLACK_CHECKBOX = [By.XPATH, '//input[@id="black"]']  # чекбокс самокат черного цвета
    SCOOTER_COLOR_GREY_CHECKBOX = [By.XPATH, '//input[@id="grey"]']  # чекбокс самокат серого цвета
    COMMENT_FIELD = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']  # поле Комментарий

    ORDER_BUTTON = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']  # кнопка Заказать

    # локаторы всплывающего окна подтверждения заказа
    NO_BUTTON = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Нет"]']  # кнопка Нет
    YES_BUTTON = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Да"]']  # кнопка Да

    # локаторы всплывающего окна успешного заказа
    VIEW_STATUS_BUTTON = [By.XPATH, '//button[text()="Посмотреть статус"]']  # кнопка Посмотреть статус
