import time

from pages.main_page import RegistrationPage


class TestAuthentication:
    class TestRegistration:

        def test_registration_user(self, driver):
            registration_page = RegistrationPage(driver, "https://www.kupibilet.ru/")
            registration_page.open()
            message = registration_page.fill_all_fields()
            assert message == "Завершите регистрацию"

