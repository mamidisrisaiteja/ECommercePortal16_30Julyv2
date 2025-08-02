import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.config_reader import config

class TestFrameworkDemo:
    def _get_base_url(self):
        base_url = config.get_base_url()
        assert base_url, "Base URL not configured in config.yaml"
        return base_url

    @pytest.mark.demo
    @pytest.mark.auth
    def test_tc_auth_01_login_with_valid_credentials(self, browser_context):
        page = browser_context['page']
        login_page = LoginPage(page)
        base_url = self._get_base_url()
        login_page.navigate_to_login_page(base_url)
        assert login_page.is_login_page_displayed(), "Login page is not displayed"
        login_page.perform_login("standard_user", "secret_sauce")
        products_page = ProductsPage(page)
        assert products_page.is_products_page_displayed(), "Products page is not displayed"

    @pytest.mark.demo
    @pytest.mark.auth
    def test_tc_auth_02_login_with_invalid_credentials(self, browser_context):
        page = browser_context['page']
        login_page = LoginPage(page)
        base_url = self._get_base_url()
        login_page.navigate_to_login_page(base_url)
        assert login_page.is_login_page_displayed(), "Login page is not displayed"
        login_page.perform_login("standard_use", "secret_sauce")
        assert login_page.is_login_page_displayed(), "Should still be on login page"

    @pytest.mark.demo
    @pytest.mark.inventory
    def test_tc_inv_01_verify_product_listing(self, browser_context):
        page = browser_context['page']
        login_page = LoginPage(page)
        base_url = self._get_base_url()
        login_page.navigate_to_login_page(base_url)
        login_page.perform_login("standard_user", "secret_sauce")
        products_page = ProductsPage(page)
        assert products_page.is_products_page_displayed(), "Products page is not displayed"
        assert products_page.verify_add_to_cart_buttons_present(), "Add to cart buttons not found"

    @pytest.mark.demo
    @pytest.mark.inventory
    def test_tc_inv_02_sort_products_by_name_a_to_z(self, browser_context):
        page = browser_context['page']
        login_page = LoginPage(page)
        base_url = self._get_base_url()
        login_page.navigate_to_login_page(base_url)
        login_page.perform_login("standard_user", "secret_sauce")
        products_page = ProductsPage(page)
        assert products_page.is_products_page_displayed(), "Products page is not displayed"
        products_page.sort_products_by_name_a_to_z()
        assert products_page.verify_products_sorted_alphabetically(), "Products are not sorted alphabetically"

    @pytest.mark.demo
    @pytest.mark.cart
    def test_tc_cart_01_view_cart_contents(self, browser_context):
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
