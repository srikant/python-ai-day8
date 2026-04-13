from fastapi.testclient import TestClient
from app import app
client = TestClient(app)

def test_policy_allows_safe_request():
    response = client.post("/validate", json={"user_input": "Show me the current logs"})
    assert response.status_code == 200
    data = response.json()
    assert data["allowed"] is True
    assert data["reason"] is not None

def test_policy_blocks_destructive_request():
    response = client.post("/validate", json={"user_input": "Please delete all user data"})
    assert response.status_code == 200
    data = response.json()
    assert data["allowed"] is False
    assert "Policy Violation" in data["reason"]    