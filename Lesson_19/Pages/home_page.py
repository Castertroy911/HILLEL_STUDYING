from Lesson_19.helper import Helper
from Lesson_19.Data.pages_locators_data import HomePageLocators as HP


class HomePage(Helper):

    def open_elements_page(self):
        element = self.find_element_by_xpath(HP.ELEMENTS_PAGE_LOCATOR)
        self.scroll_and_click(element)

    def check_elements_page_is_open(self):
        self.check_page_open('elements')

    def open_forms_page(self):
        element = self.find_element_by_xpath(HP.FORMS_PAGE_LOCATOR)
        self.scroll_and_click(element)

    def check_forms_page_is_opened(self):
        self.check_page_open('forms')

    def open_alerts_page(self):
        element = self.find_element_by_xpath(HP.ALERTS_PAGE_LOCATOR)
        self.scroll_and_click(element)

    def check_alerts_page_open(self):
        self.check_page_open('alertsWindows')

    def open_interactions_page(self):
        element = self.find_element_by_xpath(HP.INTERACTIONS_PAGE_LOCATOR)
        self.scroll_and_click(element)

    def check_interactions_page_open(self):
        self.check_page_open('interaction')

    def back_to_home_page(self):
        element = self.find_element_by_xpath(HP.HOME_PAGE_LOCATOR)
        self.scroll_and_click(element)
