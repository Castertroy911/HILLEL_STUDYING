from Lesson_19.Pages.home_page import HomePage
from Lesson_19.Data.pages_locators_data import ElementsPageLocators as EP
from Lesson_19.Data.pages_locators_data import TextBoxPageLocators as TBL
from Lesson_19.Data.pages_locators_data import CheckBoxPageLocators as CBL
from Lesson_19.Data.pages_locators_data import RadioButtonPageLocators as RBL
from Lesson_19.Data.pages_data import TextBoxPageData as TBD


class ElementsPage(HomePage):

    def open_text_box_page(self):
        element = self.find_element_by_xpath(EP.TEXT_BOX_PAGE_LOCATOR)
        self.scroll_and_click(element)

    def open_check_box_page(self):
        element = self.find_element_by_xpath(EP.CHECK_BOX_PAGE_LOCATOR)
        self.scroll_and_click(element)

    def open_radio_button_page(self):
        element = self.find_element_by_xpath(EP.RADIO_BUTTON_PAGE_LOCATOR)
        self.scroll_and_click(element)


class TextBoxPage(ElementsPage):

    def enter_full_name(self):
        element = self.find_element_by_xpath(TBL.ENTER_FULL_NAME_LOCATOR)
        self.scroll_to_element(element)
        element.send_keys(TBD.FULL_NAME)

    def enter_email(self):
        element = self.find_element_by_xpath(TBL.ENTER_EMAIL_LOCATOR)
        self.scroll_to_element(element)
        element.send_keys(TBD.EMAIL)

    def enter_current_address(self):
        element = self.find_element_by_xpath(TBL.ENTER_CURRENT_ADDRESS_LOCATOR)
        self.scroll_to_element(element)
        element.send_keys(TBD.CURRENT_ADDRESS)

    def enter_permanent_address(self):
        element = self.find_element_by_xpath(TBL.ENTER_PERMANENT_ADDRESS_LOCATOR)
        self.scroll_to_element(element)
        element.send_keys(TBD.PERMANENT_ADDRESS)

    def press_submit_button(self):
        element = self.find_element_by_xpath(TBL.SUBMIT_BUTTON_LOCATOR)
        self.scroll_and_click(element)

    def check_full_name(self):
        name = self.find_element_by_xpath(TBL.CHECK_FULL_NAME_LOCATOR)
        self.scroll_to_element(name)
        name = name.text
        assert TBD.FULL_NAME in name, 'Full name is not saved or saved incorrect'

    def check_email(self):
        email = self.find_element_by_xpath(TBL.CHECK_EMAIL_LOCATOR)
        self.scroll_to_element(email)
        email = email.text
        assert TBD.EMAIL in email, 'Email is not saved or saved incorrect'

    def check_current_address(self):
        address = self.find_element_by_xpath(TBL.CHECK_CURRENT_ADDRESS_LOCATOR)
        self.scroll_to_element(address)
        address = address.text
        assert TBD.CURRENT_ADDRESS in address, 'Current address is not saved or saved incorrect'

    def check_permanent_address(self):
        address = self.find_element_by_xpath(TBL.CHECK_PERMANENT_ADDRESS_LOCATOR)
        self.scroll_to_element(address)
        address = address.text
        assert TBD.PERMANENT_ADDRESS in address, 'Permanent address is not saved or saved incorrect'


class CheckBoxPage(ElementsPage):

    def select_desktop_checkbox(self):
        self.find_element_by_xpath(CBL.COLLAPSE_LIST).click()
        element = self.find_element_by_xpath(CBL.DESKTOP_CHECKBOX_LOCATOR)
        self.scroll_and_click(element)

    def select_downloads_checkbox(self):
        element = self.find_element_by_xpath(CBL.DESKTOP_CHECKBOX_LOCATOR)
        self.scroll_and_click(element)

    def check_desktop_checkbox_selected(self):
        class_data = self.find_element_by_xpath(CBL.DESKTOP_CHECKBOX_LOCATOR)
        self.scroll_to_element(class_data)
        class_data = class_data.get_attribute('class')
        assert 'check' in class_data, '"Desktop" checkbox is not selected'

    def check_downloads_checkbox_selected(self):
        class_data = self.find_element_by_xpath(CBL.DOWNLOADS_CHECKBOX_LOCATOR)
        self.scroll_to_element(class_data)
        class_data = class_data.get_attribute('class')
        assert 'check' in class_data, '"Downloads" checkbox is not selected'


class RadioButtonPage(ElementsPage):

    def select_yes_radio_button(self):
        element = self.find_element_by_xpath(RBL.YES_RADIO_BUTTON)
        self.scroll_and_click(element)

    def select_impressive_radio_button(self):
        element = self.find_element_by_xpath(RBL.IMPRESSIVE_RADIO_BUTTON)
        self.scroll_and_click(element)

    def check_yes_button_selected(self):
        text = self.find_element_by_xpath(RBL.SELECTED_BUTTON_LOCATOR)
        self.scroll_to_element(text)
        text = text.text
        assert 'yes' in text.lower(), '"Yes" radio button is not selected'

    def check_impressive_button_selected(self):
        text = self.find_element_by_xpath(RBL.SELECTED_BUTTON_LOCATOR)
        self.scroll_to_element(text)
        text = text.text
        assert 'impressive' in text.lower(), '"Impressive" radio button is not selected'

    def check_no_button_disable(self):
        class_data = self.find_element_by_xpath(RBL.NO_RADIO_BUTTON)
        self.scroll_to_element(class_data)
        class_data = class_data.get_attribute('class')
        assert 'disabled' in class_data, "'No' radio button is enabled, but it shouldn't"
