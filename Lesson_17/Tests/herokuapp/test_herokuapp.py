import pytest
from Lesson_17.Pages.herokuapp.checkboxes_page import CheckboxesPage
from Lesson_17.Pages.herokuapp.dropdown_list_page import DropdownListPage
from Lesson_17.Pages.herokuapp.disappearing_elements_page import DisappearingElementsPage


@pytest.mark.herokuapp
@pytest.mark.all_tests
class TestHerokuappPage:

    def test_checkboxes_page(self, browser):
        page = CheckboxesPage(browser)
        page.open_home_page()
        page.open_checkboxes_page()
        page.select_first_checkbox()
        page.check_is_checkbox_selected()
        page.open_home_page()

    def test_disappearing_elements_page(self, browser):
        page = DisappearingElementsPage(browser)
        page.open_disappearing_elements_page()
        page.check_is_element_present()
        page.refresh_page()
        page.check_is_element_disappear()
        page.open_home_page()

    def test_dropdown_list_page(self, browser):
        page = DropdownListPage(browser)
        page.open_dropdown_list_page()
        page.select_option()
        page.check_is_element_selected()
        page.open_home_page()
