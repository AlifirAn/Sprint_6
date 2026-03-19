from selenium.webdriver.common.by import By

class MainPageLocators:
    #локаторы вопросов
    QUESTION_PAY = (By.XPATH, "//div[text()='Сколько это стоит? И как оплатить?']")
    QUESTION_MULTIPLE_SCOOTERS = (By.XPATH, "//div[text()='Хочу сразу несколько самокатов! Так можно?']")
    QUESTION_RENTAL_TIME = (By.XPATH, "//div[text()='Как рассчитывается время аренды?']")
    QUESTION_RENT_TODAY = (By.XPATH, "//div[text()='Можно ли заказать самокат прямо на сегодня?']")
    QUESTION_CHANGE_RENTAL_TIME = (By.XPATH, "//div[text()='Можно ли продлить заказ или вернуть самокат раньше?']")
    QUESTION_CHARGER = (By.XPATH, "//div[text()='Вы привозите зарядку вместе с самокатом?']")
    QUESTION_CANCEL_RENT = (By.XPATH, "//div[text()='Можно ли отменить заказ?']")
    QUESTION_BEYOND_MKAD = (By.XPATH, "//div[text()='Я жизу за МКАДом, привезёте?']")
    #локаторы ответов
    ANSWER_PAY = (By.XPATH, "//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    ANSWER_MULTIPLE_SCOOTERS = (By.XPATH, "//p[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")
    ANSWER_RENTAL_TIME = (By.XPATH, "//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")
    ANSWER_RENT_TODAY = (By.XPATH, "//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")
    ANSWER_CHANGE_RENTAL_TIME = (By.XPATH, "//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']")
    ANSWER_CHARGER = (By.XPATH, "//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']")
    ANSWER_CANCEL_RENT = (By.XPATH, "//p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")
    ANSWER_BEYOND_MKAD = (By.XPATH, "//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']")
    #локаторы кнопок заказать
    ORDER_BUTTON_HEADER = (By.CSS_SELECTOR, '[class="Button_Button__ra12g"]')
    ORDER_BUTTON_PAGE = (By.CSS_SELECTOR, '.Button_Button__ra12g.Button_Middle__1CSJM') #здесь поменять на XPATH?