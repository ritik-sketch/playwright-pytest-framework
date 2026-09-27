"""Page Object for the shopping cart page."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):
    path = "/cart.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_items = page.locator(".cart_item")
        self.item_names = page.locator(".inventory_item_name")
        self.checkout_button = page.locator("[data-test='checkout']")

    def get_item_names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def proceed_to_checkout(self) -> None:
        self.checkout_button.click()
