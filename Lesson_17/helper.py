from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from Lesson_17.Pages.base_page import BasePage


class Helper(BasePage):

    def is_element_present(self, xpath_selector):
        try:
            self.browser.find_element(By.XPATH, xpath_selector)
            return True
        except NoSuchElementException:
            return False
