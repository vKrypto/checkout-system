import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

@pytest.fixture
def sample_data():
    return {
        "products": ["A", "B", "A", "A", "D"]
    }

def test_checkout(sample_data):
    response = client.post("/checkout", json=sample_data)
    assert response.status_code == 200
    assert response.json() == {"total_price": 175.0} 
