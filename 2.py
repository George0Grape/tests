import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.utils import generate_short_code
client = TestClient(app)


def test_shorten_url_success():
    response = client.post("/shorten", json={"url": "https://example.com"})
    assert response.status_code == 200
    data = response.json()
    assert "short_code" in data
    assert isinstance(data["short_code"], str)
    assert len(data["short_code"]) == 6


def test_shorten_url_invalid():
    response = client.post("/shorten", json={"url": "not-a-url"})
    assert response.status_code == 422


def test_redirect_existing():
    resp_create = client.post("/shorten", json={"url": "https://example.com"})
    short_code = resp_create.json()["short_code"]
    response = client.get(f"/{short_code}", allow_redirects=False)
    assert response.status_code in (307, 302)
    assert response.headers["location"] == "https://example.com"


def test_redirect_nonexistent():
    response = client.get("/nonexistent")
    assert response.status_code == 404


def test_delete_link():
    resp_create = client.post("/shorten", json={"url": "https://test.com"})
    short_code = resp_create.json()["short_code"]
    delete_response = client.delete(f"/{short_code}")
    assert delete_response.status_code == 204
    redirect_response = client.get(f"/{short_code}", allow_redirects=False)
    assert redirect_response.status_code == 404


@patch('app.utils.generate_short_code')
def test_generate_short_code_mocked(mock_generate):
    mock_generate.return_value = 'ABC123'

    response = client.post("/shorten", json={"url": "https://mocked.com"})
    data = response.json()

    assert data["short_code"] == 'ABC123'