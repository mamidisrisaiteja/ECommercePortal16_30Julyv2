from playwright.sync_api import Page
from .base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_title = "text=Your Cart"
        self.cart_items = ".cart_item"

    def is_cart_page_displayed(self):
        return self.page.locator(self.cart_title).is_visible()

    def is_cart_empty(self):
        return self.page.locator(self.cart_items).count() == 0

    def get_cart_items_count(self):
        return self.page.locator(self.cart_items).count()

    def verify_item_in_cart(self, item_name):
        return self.page.locator(f".cart_item:has-text('{item_name}')").is_visible()
