import pytest
from fastapi.testclient import TestClient
from main import app

# Initialize test client
client = TestClient(app)


def test_root_endpoint():
    """
    ✅ Test if root endpoint returns success message and status code 200
    """
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Sentiment API is running successfully" in data["message"]


def test_predict_positive_sentiment():
    """
    ✅ Test positive sentiment prediction
    """
    response = client.post("/predict", json={"text": "I love working with AI!"})
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "positive"
    assert data["polarity"] > 0


def test_predict_negative_sentiment():
    """
    ✅ Test negative sentiment prediction
    """
    response = client.post("/predict", json={"text": "This is a horrible experience."})
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "negative"
    assert data["polarity"] < 0


def test_predict_neutral_sentiment():
    """
    ✅ Test neutral sentiment prediction
    """
    response = client.post("/predict", json={"text": "It is a table."})
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "neutral"
    assert data["polarity"] == 0


def test_empty_text_error():
    """
    🚫 Test empty text raises 400 error
    """
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Text cannot be empty"


def test_invalid_payload_structure():
    """
    🚫 Test invalid JSON structure raises 422 validation error
    """
    response = client.post("/predict", json={"wrong_key": "Hello"})
    assert response.status_code == 422


@pytest.mark.parametrize("text,expected", [
    ("I love this movie", "positive"),
    ("I hate this movie", "negative"),
    ("This is a chair", "neutral"),
])
def test_multiple_sentiments(text, expected):
    """
    ✅ Test multiple sentiment cases using parameterized test
    """
    response = client.post("/predict", json={"text": text})
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == expected
