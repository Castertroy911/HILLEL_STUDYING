import allure
from selenium.webdriver.common.by import By
from Lesson_17.helper import Helper


class HomePage(Helper):

    @allure.step('Open checkboxes page')
    def open_checkboxes_page(self):
        self.browser.find_element(By.XPATH, '//a[@href="/checkboxes"]').click()

    @allure.step('Open disappearing elements page')
    def open_disappearing_elements_page(self):
        self.browser.find_element(By.XPATH, '//a[@href="/disappearing_elements"]').click()

    @allure.step('Open dropdown list_page')
    def open_dropdown_list_page(self):
        self.browser.find_element(By.XPATH, '//a[@href="/dropdown"]').click()

    @allure.step('Open home page')
    def open_home_page(self):
        self.browser.get('http://the-internet.herokuapp.com/')
