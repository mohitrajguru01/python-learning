# Use an official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy global files
COPY ../../requirement.txt /app/requirement.txt
COPY ../../start.sh /app/start.sh

# Copy app code
COPY . /app

# Install dependencies
RUN apt-get update && apt-get install -y bash && \
    python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirement.txt && \
    chmod +x /app/start.sh

# Expose port
EXPOSE 8000

# Command for Railway
CMD ["/bin/bash", "/app/start.sh"]
