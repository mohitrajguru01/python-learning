#!/bin/bash
set -e  # Exit immediately if a command fails
python -m pip install --upgrade pip
python -m pip install -r /app/requirement.txt
exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
