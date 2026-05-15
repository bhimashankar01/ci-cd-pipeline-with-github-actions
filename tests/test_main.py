from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello FastAPI"
    }


def test_add():
    response = client.get("/add?a=10&b=20")

    assert response.status_code == 200
    assert response.json() == {
        "result": 30
    }