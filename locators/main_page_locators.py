from selenium.webdriver.common.by import By

class MainPageLocators:
    #локаторы вопросов
    QUESTION_PAY = (By.XPATH, "//div[contains(text(), 'Сколько это стоит')]")
    QUESTION_MULTIPLE_SCOOTERS = (By.XPATH, "//div[contains(text(), 'несколько самокатов')]")
    QUESTION_RENTAL_TIME = (By.XPATH, "//div[contains(text(), 'время аренды')]")
    QUESTION_RENT_TODAY = (By.XPATH, "//div[contains(text(), 'заказать самокат прямо на сегодня')]")
    QUESTION_CHANGE_RENTAL_TIME = (By.XPATH, "//div[contains(text(), 'продлить заказ или вернуть самокат раньше')]")
    QUESTION_CHARGER = (By.XPATH, "//div[contains(text(), 'Вы привозите зарядку')]")
    QUESTION_CANCEL_RENT = (By.XPATH, "//div[contains(text(), 'отменить заказ')]")
    QUESTION_BEYOND_MKAD = (By.XPATH, "//div[contains(text(), 'за МКАДом')]")
    #локаторы ответов
    ANSWER_PAY = (By.XPATH, "//p[contains(text(), '400 рублей')]")
    ANSWER_MULTIPLE_SCOOTERS = (By.XPATH, "//p[contains(text(), 'один заказ — один самокат')]")
    ANSWER_RENTAL_TIME = (By.XPATH, "//p[contains(text(), 'Отсчёт времени аренды начинается с момента')]")
    ANSWER_RENT_TODAY = (By.XPATH, "//p[contains(text(), 'Только начиная с завтрашнего дня')]")
    ANSWER_CHANGE_RENTAL_TIME = (By.XPATH, "//p[contains(text(), 'можно позвонить в поддержку')]")
    ANSWER_CHARGER = (By.XPATH, "//p[contains(text(), 'с полной зарядкой')]")
    ANSWER_CANCEL_RENT = (By.XPATH, "//p[contains(text(), 'пока самокат не привезли')]")
    ANSWER_BEYOND_MKAD = (By.XPATH, "//p[contains(text(), 'И Москве, и Московской области')]")
    #локаторы кнопок заказать
    ORDER_BUTTON_HEADER = (By.CSS_SELECTOR, ".Header_Header__214zg .Button_Button__ra12g")
    ORDER_BUTTON_PAGE = (By.CSS_SELECTOR, ".Home_RoadMap__2tal_ .Button_Button__ra12g") 