import pytest

from Lesson_17.Pages.globalsqa.home_page_globalsqa import HomePageGlobalsqa
from Lesson_17.Pages.globalsqa.user_page import UserPage


@pytest.fixture()
def user_page(browser):
    return UserPage(browser)


@pytest.fixture()
def home_page(browser):
    return HomePageGlobalsqa(browser)
