from Lesson_17.Pages.herokuapp.home_page import HomePage


class DisappearingElementsPage(HomePage):

    def check_is_element_present(self):
        element = self.is_element_present('//a[@href="/gallery/"]')
        assert element, 'Element is not present'

    def refresh_page(self):
        self.browser.refresh()

    def check_is_element_disappear(self):
        element = self.is_element_present('//a[@href="/gallery/"]')
        assert element is False, 'Element is not disappear'
