from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_authors():
    response = client.get("api/v1/authors")
    assert response.status_code == 200

