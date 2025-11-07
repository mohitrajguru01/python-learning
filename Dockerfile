# ==============================
# 1. Base Python Image
# ==============================
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# ==============================
# 2. Copy dependency file first (for caching)
# ==============================
COPY requirement.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# ==============================
# 3. Copy entire project
# ==============================
COPY py_week4/py_day25 .

# ==============================
# 4. Expose FastAPI port
# ==============================
EXPOSE 8000

# ==============================
# 5. Start command using Gunicorn + Uvicorn Worker
# ==============================
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]
