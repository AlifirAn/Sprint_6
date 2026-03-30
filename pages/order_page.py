import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from urls import Urls

class OrderPageSamokat(BasePage):
    
    @allure.step('Ввести имя')
    def set_first_name(self, first_name):
        self.send_in_input(OrderPageLocators.FIRST_NAME_FIELD, first_name)
        
    @allure.step('Ввести фамилию')
    def set_last_name(self, last_name):
        self.send_in_input(OrderPageLocators.LAST_NAME_FIELD, last_name)
    
    @allure.step('Ввести адрес')
    def set_address(self, address):
        self.send_in_input(OrderPageLocators.ADDRESS_FIELD, address)
    
    @allure.step('Выбрать станцию метро')
    def choose_metro(self):
        self.click_to_element(OrderPageLocators.METRO_STATION_FIELD)
        self.click_to_element(OrderPageLocators.METRO_STATION_CHERKIZOVSKAYA)
    
    @allure.step('Ввести номер телефона')
    def set_phone(self, phone):
        self.send_in_input(OrderPageLocators.PHONE_FIELD, phone)
        
    @allure.step('Нажать Продолжить')
    def confirm_first_step(self):
        self.click_to_element(OrderPageLocators.CONFIRMATION_FIRST_STEP_BUTTON)
    
    @allure.step('Выбрать дату')
    def choose_date(self):
        self.click_to_element(OrderPageLocators.DATE_FIELD)
        self.click_to_element(OrderPageLocators.DATE_TODAY)
    
    @allure.step('Выбрать срок аренды')
    def choose_rental_period(self):
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_DAY)
    
    @allure.step('Выбрать цвет самоката')
    def choose_color(self):
        self.click_to_element(OrderPageLocators.COLOR)
    
    @allure.step('Ввести комментарий')
    def set_comment(self, comment):
        self.send_in_input(OrderPageLocators.COMMENT_FIELD, comment)
    
    @allure.step('Нажать Заказать')
    def confirmation(self):
        self.click_to_element(OrderPageLocators.CONFIRMATION_BUTTON)
    
    @allure.step('Подтвердить заказ')
    def confirmation_in_button(self):
        self.click_to_element(OrderPageLocators.CONFIRMATION_BUTTON_MODAL)

    @allure.step('Проверить, что отобразилась модалка успешного заказа')
    def check_visibility_success_modal(self):
        modal = self.find_element_with_wait(OrderPageLocators.SUCCESS_MODAL)
        return modal.is_displayed()
    
    @allure.step('Проверить, что клик по лого Яндекса редиректит Дзен в новой вкладке')
    def check_logo_redirect_dzen(self):
        self.click_to_element(OrderPageLocators.STATUS_BUTTON)
        self.click_to_element(OrderPageLocators.YANDEX_LOGO)
        self.wait_two_windows()
        self.switch_to_window(-1)
        return self.wait_for_url_contains(Urls.DZEN_PAGE)
    
    @allure.step('Проверить, что клик по лого Самоката открывает главную страницу')
    def check_logo_open_main_page(self):
        self.switch_to_window(0)
        self.click_to_element(OrderPageLocators.SAMOKAT_LOGO)
        return self.wait_for_url(Urls.MAIN_PAGE)
    
    
        
    
    