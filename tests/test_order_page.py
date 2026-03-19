import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pages.main_page import MainPageSamokat
from pages.order_page import OrderPageSamokat
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators

class TestOrder:

    @pytest.mark.parametrize("order_locator, first_name, last_name, address, phone, comment", [
    (MainPageLocators.ORDER_BUTTON_HEADER, "Анастасия", "Иванова", "Черниговская 36", "+79000000000", "Очень жду самокат"),
    (MainPageLocators.ORDER_BUTTON_PAGE, "Абдула", "Аллаяр", "Советская улица 80к1", "+79111111111", "")
])
    def test_order_with_button_in_header(self, driver, order_locator, first_name, last_name, address, phone, comment): 
        driver.get('https://qa-scooter.praktikum-services.ru/')

        main_page = MainPageSamokat(driver)        
        main_page.click_order(order_locator)

        order_page = OrderPageSamokat(driver)
        order_page.set_first_name(first_name)
        order_page.set_last_name(last_name)
        order_page.set_address(address)
        order_page.choose_metro()
        order_page.set_phone(phone)
        order_page.confirm_first_step()
        order_page.choose_date()
        order_page.choose_rental_period()
        order_page.choose_color()
        order_page.set_comment(comment)
        order_page.confirmation()
        order_page.confirmation_in_button()
        assert order_page.check_visibility_success_modal() and order_page.check_logo_redirect_dzen() and order_page.check_logo_open_main_page()
