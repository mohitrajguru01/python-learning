#!/bin/bash
pip install -r requirement.txt
exec uvicorn py_week4.py_day25.main:app --host 0.0.0.0 --port $PORT
