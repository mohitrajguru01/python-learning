from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
import os

LOG_DIR = "py_week4/py_day26/logs"
LOG_FILE = f"{LOG_DIR}/app.log"
# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Setup logging
logging.basicConfig(
    filename="py_week4/py_day26/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Logging & Error Handling Demo - Day 26"}

@app.get("/divide")
def divide_numbers(a: float, b: float):
    try:
        result = a / b
        return {"result": result}
    except Exception as e:
        logging.error(f"Error dividing numbers: {str(e)}")
        raise e

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    error_message = f"Error: {str(exc)} | Path: {request.url.path}"
    logging.error(error_message)
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error", "detail": str(exc)}
    )

# Invalid route handler
@app.middleware("http")
async def log_invalid_requests(request: Request, call_next):
    try:
        response = await call_next(request)
        if response.status_code == 404:
            logging.warning(f"Invalid API Request - Path: {request.url.path}")
        return response
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise e
