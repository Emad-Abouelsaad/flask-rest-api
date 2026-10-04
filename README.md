# Flask REST API — Cloud Deployment

A small REST API built with **Python** and **Flask**, prepared for cloud deployment (PaaS) with **Gunicorn**, automated tests and a CI pipeline.
Built for the Application and Internet Services course at WSB University.

## Features
- JSON REST endpoints with UTC timestamps
- `/health` endpoint for the cloud platform's health checks
- Input validation (empty / too-long names) and JSON error responses (400, 404)
- Production-ready settings: debug mode off by default, port taken from the `PORT` environment variable
- **6 automated tests** (pytest) run on every push by **GitHub Actions**

## Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API status |
| GET | `/health` | Health check |
| GET | `/hello` | Greeting from the cloud |
| GET | `/greet/<name>` | Personal greeting |
| GET | `/api/info` | API name, version and endpoint list |

## Tech stack
Python 3, Flask, Gunicorn, pytest, GitHub Actions, PaaS cloud hosting

## Run locally
```bash
pip install -r requirements.txt
python app.py              # http://localhost:5000
pytest -v                  # run the tests
```

## Deploy
The `Procfile` (`web: gunicorn app:app`) lets the app run on PaaS platforms such as Render, Railway, Heroku or Azure App Service — connect the repository and the platform installs `requirements.txt` and starts Gunicorn.
