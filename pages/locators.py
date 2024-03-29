from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTER_PASSWORD_FIELD_1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTER_PASSWORD_FIELD_2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    ALERT_ADD_TO_CART = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    ALERT_COST_CART = (By.CSS_SELECTOR, ".alert-info .alertinner strong")


class BasketPageLocators():
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    CART_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")

