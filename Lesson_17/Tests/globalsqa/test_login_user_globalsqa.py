import pytest


@pytest.mark.globalsqa
@pytest.mark.all_tests
class TestLoginUser:
    def test_login_user(self, browser, home_page):
        browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        home_page.login_as_customer()
        home_page.select_name()
        home_page.click_login_button()
        home_page.check_is_user_logged_in()
