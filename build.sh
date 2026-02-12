#!/bin/bash
# Build script for local development and deployment

set -e

echo "🔨 Building Credit Risk Predictor..."
echo ""

# Check if Python exists
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.11+"
    exit 1
fi

echo "✅ Python version: $(python3 --version)"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install --upgrade pip
pip install -r backend/requirements.txt
pip install streamlit

# Train model if it doesn't exist
if [ ! -f "backend/models/xgb_credit_pipeline.pkl" ]; then
    echo "🤖 Training model..."
    cd backend
    python train_model.py
    cd ..
else
    echo "✅ Model already exists"
fi

echo ""
echo "🎉 Build complete!"
echo ""
echo "To start the servers, run:"
echo "  ./start.sh"
