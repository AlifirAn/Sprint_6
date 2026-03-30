import allure
from pages.base_page import BasePage

class MainPageSamokat(BasePage):

    @allure.step('Кликнуть по вопросу')
    def click_on_question(self, question_locator):
        self.click_to_element(question_locator)
    
    
    @allure.step('Проверить, что отобразился соответствующий ответ')
    def check_visibility_answer(self, answer_locator):
        answer = self.find_element_with_wait(answer_locator)
        return answer.is_displayed()
    
    @allure.step('Кликнуть на Заказать')
    def click_order(self, order_locator):
        self.click_to_element(order_locator)
