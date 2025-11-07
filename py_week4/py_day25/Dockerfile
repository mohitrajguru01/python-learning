# Use an official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and startup script from repo root
COPY ../../requirement.txt /app/requirement.txt
COPY ../../start.sh /app/start.sh

# Copy current folder (main.py etc.)
COPY . /app

# Ensure bash + permissions
RUN apt-get update && apt-get install -y bash && \
    chmod +x /app/start.sh && \
    python3 -m pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirement.txt

# Expose port for Railway
EXPOSE 8000

# ENTRYPOINT ensures bash executes your script properly
ENTRYPOINT ["/bin/bash", "/app/start.sh"]
