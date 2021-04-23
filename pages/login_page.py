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
        self.send_value(email, *LoginPageLocators.REGISTER_FORM_EMAIL, "email field is not presented")
        self.send_value(password, *LoginPageLocators.REGISTER_FORM_PASSWORD, "password field is not presented")
        self.send_value(password, *LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD, "confirm password field is not presented")

    def click_on_submit(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_SUBMIT), "submit button is not presented"
        submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        submit.click()
