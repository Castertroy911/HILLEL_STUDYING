import time
import allure
import pytest

from Lesson_17.Pages.herokuapp.home_page import HomePage


class DisappearingElementsPage(HomePage):

    @allure.step('Check that element present on page')
    def check_is_element_present(self):
        element = self.is_element_present('//a[@href="/gallery/"]')
        assert element, 'Element is not present'

    @pytest.mark.xfail('Site is working incorrect so sometimes it can ot disappear')
    @allure.step('Reload page to disappear element')
    def refresh_page(self):
        time.sleep(1)
        self.browser.refresh()

    @allure.step('Check that element is disappear')
    def check_is_element_disappear(self):
        element = self.is_element_present('//a[@href="/gallery/"]')
        assert element is False, 'Element is not disappear'
