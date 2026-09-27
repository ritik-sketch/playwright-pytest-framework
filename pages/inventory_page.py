"""Page Object for the products (inventory) page shown after login."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class InventoryPage(BasePage):
    path = "/inventory.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.items = page.locator(".inventory_item")
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")

    def add_to_cart(self, product_name: str) -> None:
        """Click 'Add to cart' on the card whose title matches product_name."""
        card = self.items.filter(has_text=product_name)
        card.get_by_role("button", name="Add to cart").click()

    def get_cart_count(self) -> int:
        """Number shown on the cart badge; 0 when the badge is not rendered."""
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.inner_text())

    def sort_by(self, option_value: str) -> None:
        """option_value is one of: az, za, lohi, hilo (the app's own values)."""
        self.sort_dropdown.select_option(option_value)

    def get_prices(self) -> list[float]:
        """Return all visible prices as numbers, in page order."""
        texts = self.item_prices.all_inner_texts()
        return [float(t.replace("$", "")) for t in texts]

    def open_cart(self) -> None:
        self.cart_link.click()
