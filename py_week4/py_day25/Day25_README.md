# 🚀 Day 25 – Cloud Deployment of Sentiment Analysis API

This project demonstrates the **deployment of a FastAPI-based Sentiment Analysis API** using **TextBlob** for NLP and **Railway.app** for cloud hosting.

---

## 📘 Topics Covered
- Cloud Deployment (Railway / Render / AWS EC2)
- Using `gunicorn` + `uvicorn` for production servers
- Docker containerization
- FastAPI API deployment pipeline

---

## 📂 Project Structure

```
python-learning/
│
├── Dockerfile
├── requirements.txt
├── start.sh
│
└── py_week4/
    └── py_day25/
        ├── main.py
        └── test_main.py
```

---

## ⚙️ Project Description

### 1. `main.py`
Implements a FastAPI application for sentiment prediction using **TextBlob**.  
Endpoints:
- `GET /` → Health check  
- `POST /predict` → Returns polarity and sentiment type

### 2. `requirements.txt`
Lists project dependencies including FastAPI, Uvicorn, Gunicorn, TextBlob, and pytest.

### 3. `Dockerfile`
Defines containerization setup for deployment using Python 3.12 and Gunicorn.

### 4. `start.sh`
A shell script to install dependencies and start the app with Gunicorn.

### 5. `test_main.py`
Contains API test cases using FastAPI’s `TestClient` to verify endpoints and responses.

---

## ☁️ Deployment on Railway

1. Push the project to GitHub.
2. Go to [Railway.app](https://railway.app) → Create New Project.
3. Choose **Deploy from GitHub Repository**.
4. Ensure `Dockerfile`, `requirements.txt`, and `start.sh` are at the root.
5. After successful build, you’ll see:
   ```
   Listening at: http://0.0.0.0:8000
   ```
6. Get the public URL from **Settings → Domains** (e.g., `https://python-learning-production.up.railway.app`).

---

## 🔍 API Testing

**Base URL:**  
`https://python-learning-production.up.railway.app`

| Endpoint | Method | Description |
|-----------|--------|--------------|
| `/` | GET | Health check |
| `/predict` | POST | Analyze text sentiment |

Example Input:
```json
{ "text": "I love this project!" }
```

Example Output:
```json
{ "text": "I love this project!", "polarity": 0.8, "sentiment": "positive" }
```

---

## 🧩 Common Deployment Issues

| Issue | Cause | Fix |
|-------|--------|-----|
| `python: not found` | Railway uses minimal containers | Use `python3` and proper base image |
| `pip: not found` | Missing Python installation | Use `python:3.12-slim` image |
| 502 Bad Gateway | App not responding | Ensure `gunicorn` runs and binds to `0.0.0.0:8000` |

---

## ✅ Final Result

- App deployed successfully at: **https://python-learning-production.up.railway.app/**
- Health check and sentiment endpoints working correctly.
- Deployment validated using test cases.

---

**Author:** Mohit  
**Project:** Python Learning – Week 4, Day 25  
**Date:** November 7, 2025  
**Deployment:** ✅ Successful on Railway
