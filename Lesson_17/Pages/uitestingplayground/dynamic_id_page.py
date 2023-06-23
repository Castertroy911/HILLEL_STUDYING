from selenium.webdriver.common.by import By
from Lesson_17.Pages.uitestingplayground.home_page import HomePage


class DynamicIdPage(HomePage):

    def find_and_click_button(self):
        self.browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()

    def get_current_id(self):
        id = self.browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]').get_attribute('id')
        return id

    def reload_page(self):
        self.browser.refresh()

    @staticmethod
    def check_id_changed(id_1, id_2):
        assert id_1 != id_2, 'Element ID does not changed'
