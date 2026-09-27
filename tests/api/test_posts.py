"""API tests for the /posts resource of JSONPlaceholder.

What is checked on every call: status code, response shape (JSON schema) and
data integrity (what we sent is what came back). No browser is involved, so
these run in a few hundred milliseconds and are the first thing CI executes.
"""

import pytest
from jsonschema import validate

from api.posts_api import PostsApi
from utils.data_loader import load_json

POSTS = load_json("posts.json")
POST_SCHEMA = load_json("schemas/post.json")


@pytest.fixture
def posts(api_client) -> PostsApi:
    return PostsApi(api_client)


@pytest.mark.api
@pytest.mark.smoke
def test_list_posts_returns_collection(posts: PostsApi):
    response = posts.list()

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) == 100


@pytest.mark.api
def test_get_post_matches_schema(posts: PostsApi):
    response = posts.get(1)

    assert response.status_code == 200
    # Raises jsonschema.ValidationError with a precise message on mismatch.
    validate(instance=response.json(), schema=POST_SCHEMA)


@pytest.mark.api
def test_create_post_returns_new_id(posts: PostsApi):
    payload = POSTS["new_post"]
    response = posts.create(payload)

    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 101          # the fake API always assigns the next id
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    validate(instance=body, schema=POST_SCHEMA)


@pytest.mark.api
def test_update_post_echoes_changes(posts: PostsApi):
    payload = POSTS["updated_post"]
    response = posts.update(1, payload)

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert body["title"] == payload["title"]


@pytest.mark.api
def test_delete_post_succeeds(posts: PostsApi):
    response = posts.delete(1)

    assert response.status_code == 200


@pytest.mark.api
@pytest.mark.parametrize("post_id", POSTS["invalid_ids"])
def test_get_unknown_post_returns_404(posts: PostsApi, post_id: int):
    response = posts.get(post_id)

    assert response.status_code == 404
