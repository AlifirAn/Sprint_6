from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class OrderPageSamokat():
    def __init__(self, driver):
        self.driver = driver

    def set_first_name(self, first_name):
        first_name_input = self.driver.find_element(*OrderPageLocators.FIRST_NAME_FIELD)
        first_name_input.send_keys(first_name)
    
    def set_last_name(self, last_name):
        last_name_input = self.driver.find_element(*OrderPageLocators.LAST_NAME_FIELD)
        last_name_input.send_keys(last_name)

    def set_address(self, address):
        address_input = self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD)
        address_input.send_keys(address)

    def choose_metro(self):
        self.driver.find_element(*OrderPageLocators.METRO_STATION_FIELD).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(OrderPageLocators.METRO_STATION_FIELD))
        self.driver.find_element(*OrderPageLocators.METRO_STATION_CHERKIZOVSKAYA).click()

    def set_phone(self, phone):
        phone_input = self.driver.find_element(*OrderPageLocators.PHONE_FIELD)
        phone_input.send_keys(phone)

    def confirm_first_step(self):
        button =  self.driver.find_element(*OrderPageLocators.CONFIRMATION_FIRST_STEP_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(OrderPageLocators.CONFIRMATION_FIRST_STEP_BUTTON))
        self.driver.find_element(*OrderPageLocators.CONFIRMATION_FIRST_STEP_BUTTON).click()

    def choose_date(self):
        self.driver.find_element(*OrderPageLocators.DATE_FIELD).click()
        self.driver.find_element(*OrderPageLocators.DATE_TODAY).click()

    def choose_rental_period(self):
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_FIELD).click()
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_DAY).click()

    def choose_color(self):
        self.driver.find_element(*OrderPageLocators.COLOR).click()

    def set_comment(self, comment):
        comment_input = self.driver.find_element(*OrderPageLocators.COMMENT_FIELD)
        comment_input.send_keys(comment) #+79000000000

    def confirmation(self):
        self.driver.find_element(*OrderPageLocators.CONFIRMATION_BUTTON).click()

    def confirmation_in_button(self):
        self.driver.find_element(*OrderPageLocators.CONFIRMATION_BUTTON_MODAL).click()

    def check_visibility_success_modal(self):
        modal = self.driver.find_element(*OrderPageLocators.SUCCESS_MODAL)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL))
        return modal.is_displayed()
    
    def check_logo_redirect_dzen(self):
        self.driver.find_element(*OrderPageLocators.STATUS_BUTTON).click()
        self.driver.find_element(*OrderPageLocators.YANDEX_LOGO).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.number_of_windows_to_be(2))
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])
        return WebDriverWait(self.driver, 5).until(expected_conditions.url_contains("https://dzen.ru"))
    
    def check_logo_open_main_page(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[0])
        self.driver.find_element(*OrderPageLocators.SAMOKAT_LOGO).click()
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/"))
    
    
        
    
    