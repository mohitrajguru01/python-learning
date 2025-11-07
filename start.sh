#!/bin/bash
set -e

echo "🚀 Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r /app/requirement.txt

echo "✅ Dependencies installed. Starting Uvicorn..."
exec python3 -m uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
