import allure
from Lesson_17.helper import Helper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class HomePageGlobalsqa(Helper):

    @allure.step('Login as a customer')
    def login_as_customer(self):
        button = self.browser.find_element(By.XPATH, '//button[@class="btn btn-primary btn-lg"]')
        button.click()

    @allure.step('Select name of the user')
    def select_name(self):
        select = Select(self.browser.find_element(By.ID, 'userSelect'))
        select.select_by_value('4')

    @allure.step('Click login button lo log in to the system')
    def click_login_button(self):
        button = self.browser.find_element(By.XPATH, '//button[@type="submit"]')
        button.click()

    @allure.step('Check is user logged in')
    def check_is_user_logged_in(self):
        assert self.is_element_present('//button[@class="btn logout"]'), 'User is not logged in or logged is not ' \
                                                                         'as customer'
