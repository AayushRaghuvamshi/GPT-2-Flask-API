import pytest
from src.main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_generate_endpoint(client):
    response = client.post(
        '/generate', json={'text': 'Write a story about a butterfly living in a lion den.'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'text' in data
    assert isinstance(data['text'], str)
    assert data['text']
