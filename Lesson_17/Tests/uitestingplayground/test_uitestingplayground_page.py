import allure
import pytest
from Lesson_17.Pages.uitestingplayground.client_side_delay_page import ClientsSideDelayPage
from Lesson_17.Pages.uitestingplayground.dynamic_id_page import DynamicIdPage
from Lesson_17.Pages.uitestingplayground.verify_text_page import VerifyTextPage


@allure.story('Test scope for "uitestingplayground" site')
@pytest.mark.uitestingplayground
@pytest.mark.all_tests
class TestUitestingplaygroundPage:

    def test_dynamic_id_page(self, browser):
        browser.get('http://uitestingplayground.com/home')
        page = DynamicIdPage(browser)
        page.open_dynamic_id_page()
        page.check_dynamic_page_open()
        page.find_and_click_button()
        id_1 = page.get_current_id()
        page.reload_page()
        id_2 = page.get_current_id()
        page.check_id_changed(id_1, id_2)
        page.back_to_home_page()

    def test_client_side_delay_page(self, browser):
        page = ClientsSideDelayPage(browser)
        page.open_client_side_delay_page()
        page.check_client_side_delay_page_open()
        page.press_button_and_wait()
        page.back_to_home_page()

    def test_verify_text_page(self, browser):
        page = VerifyTextPage(browser)
        page.open_verify_text_page()
        page.check_verify_page_open()
        page.verify_text()
        page.back_to_home_page()
