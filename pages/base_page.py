import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Открыть главную Яндекс Самокат')
    def open(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def click_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def send_in_input(self, locator, string):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.find_element(*locator).send_keys(string)

    def wait_two_windows(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.number_of_windows_to_be(2))

    def switch_to_window(self, window_number):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[window_number])

    def wait_for_url(self, url):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))
    
    def wait_for_url_contains(self, url):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))