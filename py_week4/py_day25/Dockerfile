FROM python:3.12-slim

WORKDIR /app

# Copy only the necessary files
COPY requirement.txt /app/requirement.txt
COPY py_week4/py_day25 /app

RUN pip install --no-cache-dir -r /app/requirement.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
