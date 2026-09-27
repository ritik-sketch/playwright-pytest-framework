"""Page Object for the Swag Labs login page.

One class per page. The class owns two things:
  1. locators  - where the elements are on the page
  2. actions   - what a user can do on the page

Tests never touch locators directly; they only call actions. If the UI
changes, the fix happens here in one place, not in every test.
"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    path = "/"

    def __init__(self, page: Page):
        super().__init__(page)
        # Locators are created once here and reused by every action below.
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def login(self, username: str, password: str) -> None:
        """Fill both fields and submit. Works for valid and invalid users;
        the test decides what to assert afterwards."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_text(self) -> str:
        """Return the red error banner text shown after a failed login."""
        return self.error_message.inner_text()
