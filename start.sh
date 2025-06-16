#!/bin/bash

# Start FastAPI (on port 8000)
uvicorn backend.main:app --host=0.0.0.0 --port=8000 &

# Wait a bit for backend to start
sleep 5

# Start Streamlit (on port 8080 — Railway uses this)
streamlit run frontend/streamlit_app.py --server.port=8080 --server.enableCORS false