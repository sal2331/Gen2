from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_tokens():
    response = client.post("/tokens", json={"text": "hello world"})
    assert response.status_code == 200
    assert response.json() == {"tokens": ["hello", "world"]}

def test_get_tokens_empty_text():
    response = client.post("/tokens", json={"text": ""})
    assert response.status_code == 200
    assert response.json() == {"tokens": []}

def test_get_tokens_invalid_request():
    response = client.post("/tokens", json={})
    assert response.status_code == 422  # Unprocessable Entity
