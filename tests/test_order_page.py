import pytest
import allure
from pages.main_page import MainPageSamokat
from pages.order_page import OrderPageSamokat
from locators.main_page_locators import MainPageLocators
from urls import Urls

class TestOrder:
    @allure.title('Проверка флоу успешного заказа через кнопку Заказать {order_locator}')
    @pytest.mark.parametrize("order_locator, first_name, last_name, address, phone, comment", [
    (MainPageLocators.ORDER_BUTTON_HEADER, "Анастасия", "Иванова", "Черниговская 36", "+79000000000", "Очень жду самокат"),
    (MainPageLocators.ORDER_BUTTON_PAGE, "Абдула", "Аллаяр", "Советская улица 80к1", "+79111111111", "")
])
    def test_order_with_button(self, driver, order_locator, first_name, last_name, address, phone, comment): 
        main_page = MainPageSamokat(driver)
        main_page.open(Urls.MAIN_PAGE)        
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
        assert order_page.check_visibility_success_modal()
        assert order_page.check_logo_redirect_dzen() 
        assert order_page.check_logo_open_main_page()
