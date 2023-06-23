from selenium.webdriver.common.by import By
from Lesson_17.Pages.uitestingplayground.home_page import HomePage


class VerifyTextPage(HomePage):
    def verify_text(self):
        text = self.browser.find_element(By.XPATH,
                                         '//div[@class="bg-primary"]/span[normalize-space(.)="Welcome UserName!"]').text
        assert text == 'Welcome UserName!', 'Text is not verified'
