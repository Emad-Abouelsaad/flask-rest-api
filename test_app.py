"""Automated tests for the Flask API (run: pytest)."""
from app import app


def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_home():
    res = client().get("/")
    assert res.status_code == 200
    assert res.get_json()["status"] == "running"


def test_health():
    res = client().get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}


def test_greet():
    res = client().get("/greet/Emad")
    assert res.get_json()["message"] == "Hello, Emad!"


def test_greet_long_name_is_trimmed():
    res = client().get("/greet/" + "x" * 200)
    assert len(res.get_json()["message"]) < 100


def test_api_info_lists_endpoints():
    data = client().get("/api/info").get_json()
    assert "/health" in data["endpoints"]


def test_unknown_endpoint_returns_json_404():
    res = client().get("/does-not-exist")
    assert res.status_code == 404
    assert res.get_json()["error"] == "Endpoint not found"
