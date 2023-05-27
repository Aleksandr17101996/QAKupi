from pages.base_page import BasePage
from locators.main_page_locators import SearchPageLocators


class RegistrationPage(BasePage):
    locators = SearchPageLocators()

    def fill_all_fields(self):
        email = "alexandr12@yandex.ru"
        password = "1234Aa"
        self.element_is_visible(self.locators.BUTTON_LOGIN).click()
        self.element_is_visible(self.locators.BUTTON_REGISTRATION).click()
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(email)
        self.element_is_visible(self.locators.INPUT_PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.INPUT_AGAIN_PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.BUTTON_REGISTER).click()
        message = self.element_is_visible(self.locators.MESSAGE_REGISTRATE).text
        return message
