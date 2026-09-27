"""Network interception with page.route().

The same technique is used to simulate API failures, slow responses or empty
payloads that are hard to reproduce manually. Here we block every image
request and check the product list still renders - the page must not depend
on images to be usable.
"""

import pytest
from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.regression
def test_products_render_when_images_fail(page: Page, users: dict):
    blocked: list[str] = []

    def block_images(route):
        blocked.append(route.request.url)
        route.abort()

    # Intercept before navigating so the very first requests are covered.
    page.route("**/*.{png,jpg,jpeg,svg}", block_images)

    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(users["valid"]["username"], users["valid"]["password"])

    # Wait until all requests (including aborted ones) have settled.
    page.wait_for_load_state("networkidle")

    inventory = InventoryPage(page)
    expect(inventory.items).to_have_count(6)
    assert len(blocked) > 0, "expected at least one image request to be intercepted"
