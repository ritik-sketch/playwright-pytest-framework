"""Environment configuration.

Everything that changes between environments (staging vs production, local vs
CI) is read from environment variables with a sensible default, so the same
tests run anywhere without editing code:

    BASE_URL=https://www.saucedemo.com pytest
"""

import os

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
