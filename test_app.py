import pytest
import requests

BASE_URL = "http://127.0.0.1:8080"  # Update this if using a different port

def test_home():
    """Test the home endpoint."""
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.text == "Welcome to the API!"

def test_add():
    """Test the addition endpoint."""
    response = requests.get(f"{BASE_URL}/add?a=10&b=5")
    assert response.status_code == 200
    assert response.json()["result"] == 15

def test_invalid_input():
    """Test the addition API with missing parameters."""
    response = requests.get(f"{BASE_URL}/add?a=10")
    assert response.status_code == 400  # Should return a bad request error
