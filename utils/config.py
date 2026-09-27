"""Environment configuration.

Everything that changes between environments (staging vs production, local vs
CI) is read from environment variables with a sensible default, so the same
tests run anywhere without editing code:

    BASE_URL=https://www.saucedemo.com pytest
    API_BASE_URL=https://jsonplaceholder.typicode.com pytest -m api
"""

import os

# UI under test (Playwright)
BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")

# API under test (requests)
API_BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
