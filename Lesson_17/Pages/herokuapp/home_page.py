from selenium.webdriver.common.by import By
from Lesson_17.helper import Helper


class HomePage(Helper):

    def open_checkboxes_page(self):
        self.browser.find_element(By.XPATH, '//a[@href="/checkboxes"]').click()

    def open_disappearing_elements_page(self):
        self.browser.find_element(By.XPATH, '//a[@href="/disappearing_elements"]').click()

    def open_dropdown_list_page(self):
        self.browser.find_element(By.XPATH, '//a[@href="/dropdown"]').click()

    def open_home_page(self):
        self.browser.get('http://the-internet.herokuapp.com/')
