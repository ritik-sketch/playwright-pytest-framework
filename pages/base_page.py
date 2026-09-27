"""Base class shared by every Page Object.

Holds the Playwright `page` and the small helpers that every page needs, so
the concrete page classes only describe what is specific to them.
"""

from playwright.sync_api import Page

from utils.config import BASE_URL


class BasePage:
    # Each page sets its own path, e.g. "/inventory.html".
    path = "/"

    def __init__(self, page: Page):
        self.page = page

    @property
    def url(self) -> str:
        return f"{BASE_URL}{self.path}"

    def goto(self) -> None:
        """Open this page directly by URL."""
        self.page.goto(self.url)
