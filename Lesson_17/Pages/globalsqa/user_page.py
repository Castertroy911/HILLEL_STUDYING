import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Lesson_17.Pages.globalsqa.home_page_globalsqa import HomePageGlobalsqa
from selenium.webdriver.support.ui import Select


class UserPage(HomePageGlobalsqa):

    @allure.step('Select currency for user')
    def select_currency(self):
        select = Select(self.browser.find_element(By.ID, 'accountSelect'))
        select.select_by_value('number:1011')

    @allure.step('Check selected currency')
    def check_selected_currency(self):
        text = self.browser.find_element(By.XPATH, '//div[@ng-hide="noAccount"]/strong[3]').text
        assert text == 'Pound', "Selected value doesn't match the currency"

    @allure.step('Add deposit for the user')
    def add_deposit(self):
        self.browser.find_element(By.XPATH, '//button[@ng-class="btnClass2"]').click()
        self.browser.find_element(By.XPATH, '//input[@ng-model="amount"]').send_keys('100')

    @allure.step('Click add deposit button')
    def click_add_deposit_button(self):
        self.browser.find_element(By.XPATH, '//button[@class="btn btn-default"]').click()

    @allure.step('Check that deposi sum is matching to the entered')
    def check_deposit_sum(self):
        deposit_sum = self.browser.find_element(By.XPATH, '//div[@ng-hide="noAccount"]/strong[2]').text
        assert deposit_sum == '100', 'Deposit is not saved'

    @allure.step('Logout from the system')
    def logout(self):
        self.browser.find_element(By.XPATH, '//button[@ng-show="logout"]').click()

    @allure.step('Check that user is logged out')
    def check_user_logout(self):
        wait = WebDriverWait(self.browser, timeout=10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@id="userSelect"]')))
        assert element, 'User is not logged out'
