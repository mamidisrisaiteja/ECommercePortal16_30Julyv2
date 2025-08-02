import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config_reader import config

@pytest.mark.auth
class TestAuthentication:
    def _get_base_url(self):
        base_url = config.get_base_url()
        assert base_url, "Base URL not configured in config.yaml"
        return base_url

    def test_login_with_valid_credentials(self, browser_context):
        page = browser_context['page']
        login_page = LoginPage(page)
        base_url = self._get_base_url()
        login_page.navigate_to_login_page(base_url)
        assert login_page.is_login_page_displayed(), "Login page is not displayed"
        login_page.perform_login("standard_user", "secret_sauce")
        products_page = ProductsPage(page)
        assert products_page.is_products_page_displayed(), "Products page is not displayed"

    def test_login_with_invalid_credentials(self, browser_context):
        page = browser_context['page']
        login_page = LoginPage(page)
        base_url = self._get_base_url()
        login_page.navigate_to_login_page(base_url)
        assert login_page.is_login_page_displayed(), "Login page is not displayed"
        login_page.perform_login("standard_use", "secret_sauce")
        assert login_page.is_login_page_displayed(), "Should still be on login page"
