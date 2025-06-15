web: uvicorn backend.main:app --host=0.0.0.0 --port=${PORT:-8000}
web: streamlit run frontend/streamlit_app.py --server.port=$PORT --server.address=0.0.0.0