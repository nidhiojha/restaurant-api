from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_restaurants():
    response = client.get("/restaurants?latitude=40.7128&longitude=-74.0060")
    assert response.status_code == 200
    assert "restaurants" in response.json()

