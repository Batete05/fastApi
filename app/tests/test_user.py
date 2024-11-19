# app/tests/test_user.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/auth/register", json={"username": "test", "password": "test"})
    assert response.status_code == 200
    assert response.json() == {"username": "test", "role": "volunteer"}
