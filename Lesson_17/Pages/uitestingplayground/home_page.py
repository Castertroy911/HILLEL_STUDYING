import allure
from selenium.webdriver.common.by import By
from Lesson_17.helper import Helper


class HomePage(Helper):

    @allure.step('Open dynamic id page')
    def open_dynamic_id_page(self):
        self.browser.find_element(By.XPATH, '//a[@href="/dynamicid"]').click()

    @allure.step('Check that dynamic page open')
    def check_dynamic_page_open(self):
        url = self.browser.current_url
        assert 'dynamicid' in url, 'Dynamic id page is not opened'

    @allure.step('Open client side delay page')
    def open_client_side_delay_page(self):
        self.browser.find_element(By.XPATH, '//a[@href="/clientdelay"]').click()

    @allure.step('Check that client side delay page open')
    def check_client_side_delay_page_open(self):
        url = self.browser.current_url
        assert 'clientdelay' in url, 'Client side delay page is not opened'

    @allure.step('Open verify text page')
    def open_verify_text_page(self):
        self.browser.find_element(By.XPATH, '//a[@href="/verifytext"]').click()

    @allure.step('Check that verify page open')
    def check_verify_page_open(self):
        url = self.browser.current_url
        assert 'verifytext' in url, 'Verify text page is not opened'

    @allure.step('Back to home page')
    def back_to_home_page(self):
        self.browser.find_element(By.XPATH, '//a[@href="/home"]').click()

    @allure.step('Check user on home page')
    def check_user_on_home_page(self):
        url = self.browser.current_url
        assert 'home'in url, 'User is not on the home page'
