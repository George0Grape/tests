import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.utils import generate_short_code
client = TestClient(app)
# ==========================
# ЮНИТ-ТЕСТЫ
# ==========================
def test_generate_short_code_length():
    code = generate_short_code()
    assert isinstance(code, str)
    assert len(code) == 6
def test_generate_short_code_characters():
    code = generate_short_code()
    for ch in code:
        assert ch.isalnum()
def test_generate_multiple_codes_unique():
    codes = {generate_short_code() for _ in range(1000)}
    assert len(codes) == 1000