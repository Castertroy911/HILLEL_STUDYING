from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Lesson_19.Pages.base_page import BasePage


class Helper(BasePage):

    def find_element_by_xpath(self, path):
        element = self.browser.find_element(By.XPATH, path)
        return element

    def check_page_open(self, page_name):
        url = self.browser.current_url
        assert page_name in url, f'"{page_name}" page is not opened'

    def scroll_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_and_click(self, element):
        self.scroll_to_element(element)
        element.click()
