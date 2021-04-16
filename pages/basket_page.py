from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), \
            "Your basket is empty message is not displayed"
