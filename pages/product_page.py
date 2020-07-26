from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button is not presented"

    def should_be_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME)
        assert product_name.text == message_product_name.text, "Product name is not matched"

    def should_be_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        message_product_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE)
        assert product_price.text == message_product_price.text, "Product price is not matched"


