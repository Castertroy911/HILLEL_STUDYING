import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Lesson_17.Pages.uitestingplayground.home_page import HomePage


class ClientsSideDelayPage(HomePage):

    @allure.step('Press button and vait for the server response')
    def press_button_and_wait(self):
        self.browser.find_element(By.XPATH, '//button[@id="ajaxButton"]').click()
        element = WebDriverWait(self.browser, 16).until(EC.presence_of_element_located((By.XPATH,
                                                                                        '//p[@class="bg-success"]')))
        assert element, 'Delayed message is not found'
