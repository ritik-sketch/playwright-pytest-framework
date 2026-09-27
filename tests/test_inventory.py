"""Inventory (products) page tests."""

import pytest
from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage


@pytest.mark.regression
def test_add_to_cart_updates_badge(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)

    assert inventory.get_cart_count() == 0
    inventory.add_to_cart("Sauce Labs Backpack")

    expect(inventory.cart_badge).to_have_text("1")


@pytest.mark.regression
def test_sort_by_price_low_to_high(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)

    inventory.sort_by("lohi")
    prices = inventory.get_prices()

    # The list the user sees must equal the same list sorted ascending.
    assert prices == sorted(prices)
    assert len(prices) == 6
