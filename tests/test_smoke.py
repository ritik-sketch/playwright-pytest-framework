"""Smoke checks: is the app up and reachable at all?"""

import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@pytest.mark.smoke
def test_homepage_loads(page: Page):
    LoginPage(page).goto()
    expect(page).to_have_title("Swag Labs")
