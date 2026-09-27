"""Login tests for Swag Labs.

Each test reads like a user story: open page -> do action -> check result.
All page interaction goes through LoginPage (Page Object Model), so these
tests contain no selectors.
"""

import re

import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from utils.data_loader import load_json

# Loaded at import time so pytest can build one test per row (parametrize).
INVALID_LOGINS = load_json("users.json")["invalid_logins"]


@pytest.mark.smoke
def test_valid_user_can_login(page: Page, users: dict):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(users["valid"]["username"], users["valid"]["password"])

    # A successful login lands on the inventory (products) page.
    expect(page).to_have_url(re.compile(r".*/inventory\.html"))


@pytest.mark.regression
@pytest.mark.parametrize("case", INVALID_LOGINS, ids=[c["id"] for c in INVALID_LOGINS])
def test_invalid_login_shows_error(page: Page, case: dict):
    """Data-driven negative tests: one row in users.json = one test case."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(case["username"], case["password"])

    expect(login_page.error_message).to_be_visible()
    assert case["expected_error"] in login_page.get_error_text()
