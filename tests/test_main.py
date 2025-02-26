import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_work_excuse():
    response = client.get("/work-excuse")
    assert response.status_code == 200
    assert "excuse" in response.json()

def test_get_late_excuse():
    response = client.get("/late-excuse")
    assert response.status_code == 200
    assert "excuse" in response.json()

def test_get_help_excuse():
    response = client.get("/help-excuse")
    assert response.status_code == 200
    assert "excuse" in response.json()

def test_get_busy_excuse():
    response = client.get("/busy-excuse")
    assert response.status_code == 200
    assert "excuse" in response.json()

def test_get_homework_excuse():
    response = client.get("/homework-excuse")
    assert response.status_code == 200
    assert "excuse" in response.json()

def test_get_chore_excuse():
    response = client.get("/chore-excuse")
    assert response.status_code == 200
    assert "excuse" in response.json()

def test_get_custom_excuse():
    response = client.get("/custom-excuse?prompt=Generate%20a%20custom%20excuse&system_role=You%20are%20an%20excuse%20generator.%20Provide%20a%20brief,%20creative,%20and%20plausible%20excuse.")
    assert response.status_code == 200
    assert "excuse" in response.json()