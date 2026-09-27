"""Service object for the /posts resource.

The API equivalent of a Page Object: tests call `posts.create(...)` instead of
building URLs and payloads themselves. If an endpoint changes, this is the
only file that changes.
"""

import requests

from api.client import ApiClient


class PostsApi:
    PATH = "/posts"

    def __init__(self, client: ApiClient):
        self.client = client

    def list(self) -> requests.Response:
        return self.client.get(self.PATH)

    def get(self, post_id: int) -> requests.Response:
        return self.client.get(f"{self.PATH}/{post_id}")

    def create(self, payload: dict) -> requests.Response:
        return self.client.post(self.PATH, json=payload)

    def update(self, post_id: int, payload: dict) -> requests.Response:
        return self.client.put(f"{self.PATH}/{post_id}", json=payload)

    def delete(self, post_id: int) -> requests.Response:
        return self.client.delete(f"{self.PATH}/{post_id}")
