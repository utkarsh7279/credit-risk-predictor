#!/bin/bash

# Start the FastAPI backend in background
uvicorn backend.main:app --host=0.0.0.0 --port=8000 &

# Wait for backend to start (optional: increase sleep time if needed)
sleep 5

# Start Streamlit frontend
streamlit run frontend/streamlit_app.py --server.port 8080 --server.address 0.0.0.0