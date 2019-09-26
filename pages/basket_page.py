from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "Items in the basket exist"

    def should_be_text_that_the_basket_is_empty(self):
        text_that_the_basket_is_empty = self.browser.find_element(*BasketPageLocators.CART_IS_EMPTY).text
        assert "Your basket is empty." in text_that_the_basket_is_empty, \
            "No text that the basket is empty"

