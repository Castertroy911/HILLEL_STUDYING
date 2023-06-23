from Lesson_17.helper import Helper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class HomePageGlobalsqa(Helper):
    def login_as_customer(self):
        button = self.browser.find_element(By.XPATH, '//button[@class="btn btn-primary btn-lg"]')
        button.click()

    def select_name(self):
        select = Select(self.browser.find_element(By.ID, 'userSelect'))
        select.select_by_value('4')

    def click_login_button(self):
        button = self.browser.find_element(By.XPATH, '//button[@type="submit"]')
        button.click()

    def check_is_user_logged_in(self):
        assert self.is_element_present('//button[@class="btn logout"]'), 'User is not logged in or logged is not ' \
                                                                         'as customer'
