"""
Flask REST API deployed to the cloud.

Run locally:      python app.py
Run in production: gunicorn app:app
"""

import os
from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)

API_NAME = "Cloud Services API"
API_VERSION = "1.1"
MAX_NAME_LENGTH = 50


def now_iso():
    """Current UTC time in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Cloud Services API",
        "status": "running",
        "timestamp": now_iso(),
    })


@app.route("/health")
def health():
    """Health-check endpoint for the cloud platform / load balancer."""
    return jsonify({"status": "ok"}), 200


@app.route("/hello")
def hello():
    return jsonify({
        "message": "Hello from the cloud!",
        "timestamp": now_iso(),
    })


@app.route("/greet/<name>")
def greet(name):
    name = name.strip()[:MAX_NAME_LENGTH]
    if not name:
        return jsonify({"error": "Name must not be empty"}), 400
    return jsonify({
        "message": f"Hello, {name}!",
        "timestamp": now_iso(),
    })


@app.route("/api/info")
def api_info():
    return jsonify({
        "api_name": API_NAME,
        "version": API_VERSION,
        "endpoints": ["/", "/health", "/hello", "/greet/<name>", "/api/info"],
    })


@app.errorhandler(404)
def not_found(_error):
    return jsonify({"error": "Endpoint not found"}), 404


if __name__ == "__main__":
    # Debug mode only when explicitly enabled; the cloud platform sets PORT.
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=debug)
