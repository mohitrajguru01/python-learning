#!/bin/bash
echo "🚀 Installing dependencies..."
pip install --no-cache-dir -r requirement.txt

echo "🔥 Starting FastAPI server..."
exec uvicorn py_week4.py_day25.main:app --host 0.0.0.0 --port ${PORT:-8000}
