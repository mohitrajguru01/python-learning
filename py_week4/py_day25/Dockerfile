# Use an official Python base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirement.txt /app/requirement.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy app source code
COPY py_week4/py_day25 /app

# Expose FastAPI default port
EXPOSE 8000

# Command for production: Gunicorn + Uvicorn workers
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]
