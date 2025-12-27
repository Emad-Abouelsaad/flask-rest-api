from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to my Flask API!",
        "status": "running",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/hello')
def hello():
    return jsonify({
        "message": "Hello from the cloud!",
        "task": "Task 2 - Flask API Deployment",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/greet/<name>')
def greet(name):
    return jsonify({
        "message": f"Hello, {name}!",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/info')
def api_info():
    return jsonify({
        "api_name": "University Cloud Services API",
        "version": "1.0",
        "endpoints": [
            "/",
            "/hello",
            "/greet/<name>",
            "/api/info"
        ]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)