import allure
from selenium.webdriver.common.by import By
from Lesson_17.Pages.uitestingplayground.home_page import HomePage


class DynamicIdPage(HomePage):

    @allure.step('Find and click button')
    def find_and_click_button(self):
        self.browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()

    @allure.step('Get the current "ID" value')
    def get_current_id(self):
        id = self.browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]').get_attribute('id')
        return id

    @allure.step('Reload page')
    def reload_page(self):
        self.browser.refresh()

    @staticmethod
    @allure.step('Check that id is changed')
    def check_id_changed(id_1, id_2):
        assert id_1 != id_2, 'Element ID does not changed'
