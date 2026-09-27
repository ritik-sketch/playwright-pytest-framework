"""Small helper to load JSON test data from the data/ folder."""

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_json(file_name: str) -> dict:
    """Return the parsed content of data/<file_name>."""
    with open(DATA_DIR / file_name, encoding="utf-8") as f:
        return json.load(f)
