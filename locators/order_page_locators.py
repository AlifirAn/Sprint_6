from selenium.webdriver.common.by import By

class OrderPageLocators:
    #первый шаг
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '[placeholder="* Имя"]')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_FIELD = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')
    METRO_STATION_CHERKIZOVSKAYA = (By.XPATH, "//div[text()='Черкизовская']") 
    PHONE_FIELD = (By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]')
    CONFIRMATION_FIRST_STEP_BUTTON = (By.XPATH, "//button[text()='Далее']") 
    #второй шаг
    DATE_FIELD = (By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')
    DATE_TODAY = (By.CSS_SELECTOR, ".react-datepicker__day--today")
    RENTAL_PERIOD_FIELD = (By.CSS_SELECTOR, '.Dropdown-arrow')
    RENTAL_PERIOD_DAY = (By.XPATH, "//div[text()='сутки']") 
    COLOR = (By.ID, "black") 
    COMMENT_FIELD = (By.CSS_SELECTOR, '[placeholder="Комментарий для курьера"]')
    CONFIRMATION_BUTTON = (By.CSS_SELECTOR, '[class="Button_Button__ra12g Button_Middle__1CSJM"]')
    CONFIRMATION_BUTTON_MODAL = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[text()='Заказ оформлен']")
    STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
    YANDEX_LOGO = (By.CSS_SELECTOR, '[src="/assets/ya.svg"]')
    SAMOKAT_LOGO = (By.CSS_SELECTOR, '[src="/assets/scooter.svg"]')
