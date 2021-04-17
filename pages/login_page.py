from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def fill_register_from(self, email, password):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_EMAIL), "email is not presented"
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        password_field1.send_keys(password)
        password_field2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD)
        password_field2.send_keys(password)

    def click_on_submit(self):
        submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        submit.click()
