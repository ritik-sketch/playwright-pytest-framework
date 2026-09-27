"""End-to-end purchase journey: login -> add products -> cart -> checkout -> done."""

import re

import pytest
from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from utils.data_loader import load_json


@pytest.mark.e2e
def test_complete_purchase_flow(logged_in_page: Page):
    data = load_json("checkout.json")
    products = data["products"]
    customer = data["customer"]

    inventory = InventoryPage(logged_in_page)
    for name in products:
        inventory.add_to_cart(name)
    assert inventory.get_cart_count() == len(products)

    inventory.open_cart()
    cart = CartPage(logged_in_page)
    expect(logged_in_page).to_have_url(re.compile(r".*/cart\.html"))
    assert cart.get_item_names() == products

    cart.proceed_to_checkout()
    checkout = CheckoutPage(logged_in_page)
    checkout.fill_customer_info(
        customer["first_name"], customer["last_name"], customer["postal_code"]
    )
    expect(logged_in_page).to_have_url(re.compile(r".*/checkout-step-two\.html"))
    expect(checkout.summary_total).to_be_visible()

    checkout.finish_order()
    expect(logged_in_page).to_have_url(re.compile(r".*/checkout-complete\.html"))
    assert checkout.get_confirmation_text() == "Thank you for your order!"
