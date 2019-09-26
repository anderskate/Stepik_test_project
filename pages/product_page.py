from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.should_be_button_to_add_to_cart()
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button_add_to_cart.click()

    def should_be_button_to_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Button to add to cart is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def message_should_be_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message not disappear"

    def should_be_a_message_that_product_added_to_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_adding_products = self.browser.find_element(*ProductPageLocators.ALERT_ADD_TO_CART).text
        assert product_name == alert_adding_products, "Product not added to cart"

    def should_be_a_message_with_cart_cost(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_cart_cost = self.browser.find_element(*ProductPageLocators.ALERT_COST_CART).text
        assert product_price == alert_cart_cost, "Cart cost not match the price of the goods"

