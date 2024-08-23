from selenium.webdriver.common.by import By


class MainPageLocators:
    POPUP_WINDOW = [By.CLASS_NAME, 'App_CookieButton__3cvqF']  # всплывающее окно о куках
    QUESTIONS_COMMON = [By.ID, 'accordion__heading-{}']  # локаторы вопросов
    ANSWERS_COMMON = [By.XPATH, '//*[@id = "accordion__panel-{}"]/p']  # локаторы ответов
    QUESTIONS_LAST = [By.ID, 'accordion__heading-7']  # локатор последнего ответа
