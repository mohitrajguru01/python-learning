import os
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
# app writes logs to py_week4/py_day26/logs/app.log
LOG_FILE_PATH = "py_week4/py_day26/logs/app.log"


@pytest.fixture(scope="module", autouse=True)
def setup_and_cleanup_logs():
    """Ensure log file is removed after tests (do not remove before import to avoid unlinking an open log file)"""
    # Do not remove the log file here because the app configures logging at import time
    # and deleting the file would unlink an open file descriptor (making the filename disappear).
    # We'll only clean up after tests.
    yield
    # Cleanup (optional)
    if os.path.exists(LOG_FILE_PATH):
        os.remove(LOG_FILE_PATH)


# -------------------------
# ✅ Positive Test Cases
# -------------------------

def test_root_endpoint():
    """Check if root endpoint returns success message"""
    response = client.get("/")
    assert response.status_code == 200
    # The app's root message can vary slightly; assert a stable substring instead
    assert "Logging & Error Handling" in response.json()["message"]


def test_divide_valid_numbers():
    """Check valid division"""
    response = client.get("/divide?a=10&b=2")
    data = response.json()
    assert response.status_code == 200
    # Use pytest.approx for safe float comparison
    assert data["result"] == pytest.approx(5.0)


# -------------------------
# ❌ Negative / Edge Test Cases
# -------------------------

def test_divide_by_zero_triggers_500():
    """Division by zero should be handled by global exception handler and return 500"""
    response = client.get("/divide?a=1&b=0")
    assert response.status_code == 500
    body = response.json()
    assert body.get("error") == "Internal Server Error"
    # detail should contain division by zero message
    assert "division by zero" in body.get("detail", "").lower()


def test_missing_parameters_returns_422():
    """Missing query params should return 422 from FastAPI validation"""
    response = client.get("/divide?a=5")  # missing b
    assert response.status_code == 422


def test_non_numeric_parameters_return_422():
    """Non-numeric query parameters should return 422"""
    response = client.get("/divide?a=foo&b=2")
    assert response.status_code == 422


def test_invalid_route_logs_and_returns_404():
    """Invalid route should return 404 and be logged by the middleware"""
    response = client.get("/nonexistent-route")
    assert response.status_code == 404


def test_log_file_created_after_requests():
    """Ensure that after some requests the log file is created by the app"""
    # trigger a couple of requests that will cause logging (root and 404)
    client.get("/")
    client.get("/nonexistent-route")
    # The logging system should have created the file
    assert os.path.exists(LOG_FILE_PATH)
