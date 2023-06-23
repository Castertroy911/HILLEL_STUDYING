import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Lesson_17.Pages.herokuapp.home_page import HomePage


class DropdownListPage(HomePage):

    @allure.step('Select option "1"')
    def select_option(self):
        select = Select(self.browser.find_element(By.XPATH, '//select[@id="dropdown"]'))
        select.select_by_value('1')

    @allure.step('Check that option is selected')
    def check_is_element_selected(self):
        element = self.browser.find_element(By.XPATH, '//option[@value="1"]').is_selected()
        assert element, 'Value is not selected'
