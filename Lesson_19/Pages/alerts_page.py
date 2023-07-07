from Lesson_19.Pages.home_page import HomePage
from Lesson_19.Data.pages_locators_data import AllertsPageLocators as AP
from Lesson_19.Data.pages_locators_data import BrowserWindowPageLocators as BW


class AlertsPage(HomePage):

    def open_browser_windows_page(self):
        self.find_element_by_xpath(AP.BROWSER_WINDOWS).click()


class BrowserWindowsPage(AlertsPage):

    def open_new_tab(self):
        self.find_element_by_xpath(BW.NEW_TAB).click()

    def check_text_in_new_tab(self):
        self.switch_to_new_window(1)
        text = self.find_element_by_xpath(BW.TEXT_ON_NEW_TAB).text
        assert text == 'This is a sample page', 'Text in new tab is not correct'
        self.browser.close()
        self.switch_to_new_window(0)

    def open_new_window(self):
        self.find_element_by_xpath(BW.NEW_WINDOW).click()

    def check_text_in_new_window(self):
        self.switch_to_new_window(1)
        text = self.find_element_by_xpath(BW.TEXT_IN_NEW_WINDOW).text
        assert text == 'This is a sample page', 'Text in new window is not correct'
        self.browser.close()
        self.switch_to_new_window(0)

