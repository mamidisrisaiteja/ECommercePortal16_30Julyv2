import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.config_reader import config

@pytest.mark.cart
class TestCart:
    def _get_base_url(self):
        base_url = config.get_base_url()
        assert base_url, "Base URL not configured in config.yaml"
        return base_url

    def test_view_cart_contents(self, browser_context):
        page = browser_context['page']
        login_page = LoginPage(page)
        base_url = self._get_base_url()
        login_page.navigate_to_login_page(base_url)
        login_page.perform_login("standard_user", "secret_sauce")
        products_page = ProductsPage(page)
        assert products_page.is_products_page_displayed(), "Products page is not displayed"
        products_page.add_product_to_cart(0)
        products_page.click_cart_icon()
        cart_page = CartPage(page)
        assert cart_page.is_cart_page_displayed(), "Cart page is not displayed"
        assert not cart_page.is_cart_empty(), "Cart should contain items"
