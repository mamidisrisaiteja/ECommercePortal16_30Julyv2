import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config_reader import config

@pytest.mark.inventory
class TestInventory:
    def _get_base_url(self):
        base_url = config.get_base_url()
        assert base_url, "Base URL not configured in config.yaml"
        return base_url

    def test_verify_product_listing(self, browser_context):
        page = browser_context['page']
        login_page = LoginPage(page)
        base_url = self._get_base_url()
        login_page.navigate_to_login_page(base_url)
        login_page.perform_login("standard_user", "secret_sauce")
        products_page = ProductsPage(page)
        assert products_page.is_products_page_displayed(), "Products page is not displayed"
        assert products_page.verify_add_to_cart_buttons_present(), "Add to cart buttons not found"

    def test_sort_products_by_name_a_to_z(self, browser_context):
        page = browser_context['page']
        login_page = LoginPage(page)
        base_url = self._get_base_url()
        login_page.navigate_to_login_page(base_url)
        login_page.perform_login("standard_user", "secret_sauce")
        products_page = ProductsPage(page)
        assert products_page.is_products_page_displayed(), "Products page is not displayed"
        products_page.sort_products_by_name_a_to_z()
        assert products_page.verify_products_sorted_alphabetically(), "Products are not sorted alphabetically"
