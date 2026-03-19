import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pages.main_page import MainPageSamokat
from locators.main_page_locators import MainPageLocators

class TestQuestions:

    @pytest.mark.parametrize("question_locator, answer_locator", [
    (MainPageLocators.QUESTION_PAY, MainPageLocators.ANSWER_PAY),
    (MainPageLocators.QUESTION_MULTIPLE_SCOOTERS, MainPageLocators.ANSWER_MULTIPLE_SCOOTERS),
    (MainPageLocators.QUESTION_RENTAL_TIME, MainPageLocators.ANSWER_RENTAL_TIME),
    (MainPageLocators.QUESTION_RENT_TODAY, MainPageLocators.ANSWER_RENT_TODAY),
    (MainPageLocators.QUESTION_CHANGE_RENTAL_TIME, MainPageLocators.ANSWER_CHANGE_RENTAL_TIME),
    (MainPageLocators.QUESTION_CHARGER, MainPageLocators.ANSWER_CHARGER),
    (MainPageLocators.QUESTION_CANCEL_RENT, MainPageLocators.ANSWER_CANCEL_RENT),
    (MainPageLocators.QUESTION_BEYOND_MKAD, MainPageLocators.ANSWER_BEYOND_MKAD)
])
    def test_answer_mathes_question(self, driver, question_locator, answer_locator): 
        driver.get('https://qa-scooter.praktikum-services.ru/')

        main_page = MainPageSamokat(driver)        
        main_page.click_on_question(question_locator)
        assert main_page.check_visibility_answer(answer_locator) is True