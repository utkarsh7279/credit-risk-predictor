#!/bin/bash
# Start both backend and frontend servers

set -e

echo "🚀 Starting Credit Risk Predictor"
echo ""
echo "📡 Backend: http://localhost:8000"
echo "🎨 Frontend: http://localhost:8501"
echo ""

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Start backend (FastAPI)
echo "Starting backend..."
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
cd ..

# Wait for backend to start
sleep 2

# Start frontend (Streamlit)
echo "Starting frontend..."
streamlit run frontend/streamlit_app.py --server.port 8501 --client.showErrorDetails true

# Cleanup on exit
trap "kill $BACKEND_PID 2>/dev/null || true" EXIT