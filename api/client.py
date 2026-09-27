"""Thin HTTP client used by every API test.

Wraps requests.Session so that:
  - the base URL is set once (from utils.config.API_BASE_URL)
  - every request carries the same default headers
  - every request/response is logged, which makes CI failures readable
"""

import logging

import requests

from utils.config import API_BASE_URL

log = logging.getLogger("api")


class ApiClient:
    def __init__(self, base_url: str = API_BASE_URL, timeout: int = 15):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{path}"
        response = self.session.request(method, url, timeout=self.timeout, **kwargs)
        log.info("%s %s -> %s (%.0f ms)", method, url, response.status_code,
                 response.elapsed.total_seconds() * 1000)
        return response

    def get(self, path: str, **kwargs) -> requests.Response:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs) -> requests.Response:
        return self.request("POST", path, **kwargs)

    def put(self, path: str, **kwargs) -> requests.Response:
        return self.request("PUT", path, **kwargs)

    def patch(self, path: str, **kwargs) -> requests.Response:
        return self.request("PATCH", path, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        return self.request("DELETE", path, **kwargs)
