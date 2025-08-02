from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click_element(self, selector):
        self.page.click(selector)

    def fill_text(self, selector, text):
        self.page.fill(selector, text)

    def verify_text_present(self, text):
        return self.page.locator(f"text={text}").is_visible()

    def wait_for_element(self, selector, timeout=5000):
        self.page.wait_for_selector(selector, timeout=timeout)

    def take_screenshot(self, path):
        self.page.screenshot(path=path)
