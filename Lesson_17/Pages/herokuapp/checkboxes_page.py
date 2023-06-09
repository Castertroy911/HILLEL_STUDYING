import allure
from selenium.webdriver.common.by import By
from Lesson_17.Pages.herokuapp.home_page import HomePage


class CheckboxesPage(HomePage):

    @allure.step('Select first checkbox')
    def select_first_checkbox(self):
        self.browser.find_element(By.XPATH, '//form[@id="checkboxes"]/input[1]').click()

    @allure.step('Check that first checkbox is selected')
    def check_is_checkbox_selected(self):
        element = self.browser.find_element(By.XPATH, '//form[@id="checkboxes"]/input[1]').is_selected()
        assert element, 'Checkpox is not selected'
