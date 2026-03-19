from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class MainPageSamokat():
    def __init__(self, driver):
        self.driver = driver

    def click_on_question(self, question_locator):
        question =  self.driver.find_element(*question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(question_locator))
        self.driver.find_element(*question_locator).click()

    def check_visibility_answer(self, answer_locator):
        answer = self.driver.find_element(*answer_locator)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(answer_locator))
        return answer.is_displayed()
    
    #def click_order_in_header(self):
    #    self.driver.find_element(*MainPageLocators.ORDER_BUTTON_HEADER).click()

    def click_order(self, order_locator):
        button = self.driver.find_element(*order_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.driver.find_element(*order_locator).click()

