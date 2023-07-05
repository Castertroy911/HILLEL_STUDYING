class HomePageLocators:
    ELEMENTS_PAGE_LOCATOR = '//h5[contains(text(), "Elements")]'
    FORMS_PAGE_LOCATOR = '//h5[contains(text(), "Forms")]'
    ALERTS_PAGE_LOCATOR = '//h5[contains(text(), "Alerts, Frame & Windows")]'
    INTERACTIONS_PAGE_LOCATOR = '//h5[contains(text(), "Interactions")]'
    HOME_PAGE_LOCATOR = '//header/a'


class ElementsPageLocators:
    TEXT_BOX_PAGE_LOCATOR = '//li[@id="item-0"]/span[contains(text(), "Text Box")]'
    CHECK_BOX_PAGE_LOCATOR = '//li[@id="item-1"]/span[contains(text(), "Check Box")]'
    RADIO_BUTTON_PAGE_LOCATOR = '//li[@id="item-2"]/span[contains(text(), "Radio Button")]'


class TextBoxPageLocators:
    ENTER_FULL_NAME_LOCATOR = '//input[@id="userName"]'
    ENTER_EMAIL_LOCATOR = '//input[@id="userEmail"]'
    ENTER_CURRENT_ADDRESS_LOCATOR = '//textarea[@id="currentAddress"]'
    ENTER_PERMANENT_ADDRESS_LOCATOR = '//textarea[@id="permanentAddress"]'
    SUBMIT_BUTTON_LOCATOR = '//button[@id="submit"]'
    CHECK_FULL_NAME_LOCATOR = '//p[@id="name"]'
    CHECK_EMAIL_LOCATOR = '//p[@id="email"]'
    CHECK_CURRENT_ADDRESS_LOCATOR = '//p[@id="currentAddress"]'
    CHECK_PERMANENT_ADDRESS_LOCATOR = '//p[@id="permanentAddress"]'


class CheckBoxPageLocators:
    COLLAPSE_LIST = '//*[@class="rct-icon rct-icon-expand-close"]'
    DESKTOP_CHECKBOX_LOCATOR = '//span[contains(text(), "Desktop")]/preceding-sibling::span' \
                               '[@class="rct-checkbox"]/*[@stroke="currentColor"]'
    DOWNLOADS_CHECKBOX_LOCATOR = '//span[contains(text(), "Downloads")]/preceding-sibling::span' \
                                 '[@class="rct-checkbox"]/*[@stroke="currentColor"]'


class RadioButtonPageLocators:
    YES_RADIO_BUTTON = '//label[@for="yesRadio"]'
    IMPRESSIVE_RADIO_BUTTON = '//label[@for="impressiveRadio"]'
    NO_RADIO_BUTTON = '//label[@for="noRadio"]'
    SELECTED_BUTTON_LOCATOR = '//span[@class="text-success"]'
