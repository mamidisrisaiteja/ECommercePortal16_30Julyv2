from playwright.sync_api import Page
from .base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.products_title = "text=Products"
        self.add_to_cart_buttons = "button:has-text('Add to cart')"
        self.sort_icon = "select.product_sort_container"
        self.cart_icon = ".shopping_cart_link"

    def is_products_page_displayed(self):
        return self.page.locator(self.products_title).is_visible()

    def verify_add_to_cart_buttons_present(self):
        return self.page.locator(self.add_to_cart_buttons).is_visible()

    def sort_products_by_name_a_to_z(self):
        self.page.select_option(self.sort_icon, "az")

    def verify_products_sorted_alphabetically(self):
        product_names = self.page.locator('.inventory_item_name').all_text_contents()
        return product_names == sorted(product_names)

    def add_product_to_cart(self, index=0):
        self.page.locator(self.add_to_cart_buttons).nth(index).click()

    def click_cart_icon(self):
        self.page.click(self.cart_icon)
