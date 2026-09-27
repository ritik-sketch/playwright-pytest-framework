"""Page Object covering the three checkout screens:
step one (customer info) -> step two (overview) -> complete."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    path = "/checkout-step-one.html"

    def __init__(self, page: Page):
        super().__init__(page)
        # Step one
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        # Step two
        self.finish_button = page.locator("[data-test='finish']")
        self.summary_total = page.locator(".summary_total_label")
        # Complete
        self.complete_header = page.locator(".complete-header")

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def finish_order(self) -> None:
        self.finish_button.click()

    def get_confirmation_text(self) -> str:
        return self.complete_header.inner_text()
