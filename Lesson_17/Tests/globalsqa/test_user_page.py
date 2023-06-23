import allure
import pytest


@allure.story('Test scope for "globalsqa" user page')
@pytest.mark.globalsqa
@pytest.mark.all_tests
class TestUserPage:

    def test_select_currency(self, user_page):
        user_page.select_currency()
        user_page.check_selected_currency()

    def test_deposit_sum(self, user_page):
        user_page.add_deposit()
        user_page.click_add_deposit_button()
        user_page.check_deposit_sum()

    def test_user_logged_out(self, user_page):
        user_page.logout()
        user_page.check_user_logout()
