# Logging & Error Handling Demo - Day 26

This small FastAPI demo shows basic logging and error handling for a couple of endpoints.

Project layout (relevant files)

- `main.py` - FastAPI app providing endpoints:
  - `GET /` - simple health/root message
  - `GET /divide?a=<float>&b=<float>` - divides `a` by `b` and returns `{"result": <float>}`; division-by-zero returns a 500 JSON response with `detail: "division by zero"`
- `test_main.py` - pytest test suite for the app
- `logs/` - directory where the app writes `app.log`

Quick overview

- The app configures logging to write to `py_week4/py_day26/logs/app.log`.
- The `/divide` endpoint validates query parameters as floats. If `b` is zero the app logs an error and returns a JSON 500 response with a helpful `detail` field.
- A middleware logs invalid (404) requests as warnings.

Prerequisites

- Python 3.10+ (the workspace uses Python 3.12 in the dev environment but 3.10+ is sufficient)
- Virtual environment (recommended)
- Dependencies: see the project-level `requirement.txt` or install the minimal packages:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirement.txt  # if you prefer using the project's pinned deps
# or at minimum:
pip install fastapi uvicorn pytest httpx
```

Run the app locally

From the directory `py_week4/py_day26` (or the project root if you prefer), run:

```bash
# from repo root
cd py_week4/py_day26
uvicorn main:app --reload --port 8000
```

Endpoints / Examples

- Root

```bash
curl -s http://127.0.0.1:8000/ | jq
# Expected: {"message": "Logging & Error Handling Demo - Day 26"}
```

- Divide (valid)

```bash
curl -s "http://127.0.0.1:8000/divide?a=10&b=2" | jq
# Expected: {"result": 5.0}
```

- Divide by zero

```bash
curl -s -i "http://127.0.0.1:8000/divide?a=1&b=0"
# Expected HTTP 500 with JSON body like:
# {"error": "Internal Server Error", "detail": "division by zero"}
```

Testing

Run the tests for this day from the repository root (recommended) so paths match the project layout:

```bash
pytest -q py_week4/py_day26/test_main.py -q
```

This test suite covers:
- Root endpoint response
- Valid division
- Division by zero handling
- Missing / invalid query parameter validation
- Invalid route (404) behavior
- Log file creation

Logging

- Log file path (relative to repo root): `py_week4/py_day26/logs/app.log`
- The app ensures the logs directory exists and touches the log file at import time so tests and tooling can assert on its presence.

Troubleshooting

- If tests that assert the existence of the log file fail, ensure you run tests from the repository root so the expected relative paths match.
- If you see exceptions being propagated from endpoints instead of a 500 JSON response, check `main.py`'s error handling and verify that expected errors are handled (the project returns a JSONResponse for a division-by-zero case).

Next steps / Suggestions

- Add more structured logging (e.g., add request IDs) for improved observability.
- Replace string-based errors with custom exception classes and map them to proper HTTP status codes for clearer semantics.
- Add tests that assert specific log content (parse `app.log`) if you want to ensure particular messages are emitted.

License

This demo code is provided for learning and demo purposes.

