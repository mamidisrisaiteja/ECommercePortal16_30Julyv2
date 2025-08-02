from playwright.sync_api import Page
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    def navigate_to_login_page(self, base_url):
        self.page.goto(base_url)

    def is_login_page_displayed(self):
        return self.page.locator(self.login_button).is_visible()

    def perform_login(self, username, password):
        self.fill_text(self.username_input, username)
        self.fill_text(self.password_input, password)
        self.click_element(self.login_button)
