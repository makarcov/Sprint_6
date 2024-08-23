from selenium.webdriver.common.by import By


class HeaderLocators:
    YANDEX_LOGO = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']  # лого Яндекс
    SCOOTER_LOGO = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']  # лого Самокат
    ORDER_BUTTON_HEADER = [By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]']  # кнопка Заказать
    STATUS_ORDER_BUTTON = [By.CLASS_NAME, 'Header_Link__1TAG7']  # кнопка Статус заказа


class FooterLocators:
    ORDER_BUTTON_FOOTER = [By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]']  # кнопка Заказать
