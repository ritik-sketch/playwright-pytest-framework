"""Shared pytest fixtures.

pytest-playwright already provides `page` (a fresh browser tab per test).
The fixtures here build on it so tests can start from a useful state instead
of repeating the same setup lines.
"""

import re

import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from utils.data_loader import load_json


@pytest.fixture(scope="session")
def users() -> dict:
    """Test users loaded once per run from data/users.json."""
    return load_json("users.json")


@pytest.fixture
def logged_in_page(page: Page, users: dict) -> Page:
    """A page already logged in as the standard user, landed on inventory.

    Most tests need this; only the login tests start from the login page.
    """
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(users["valid"]["username"], users["valid"]["password"])
    expect(page).to_have_url(re.compile(r".*/inventory\.html"))
    return page
