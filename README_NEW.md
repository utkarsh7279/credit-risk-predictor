# Credit Risk Predictor 💳

An AI-powered credit risk prediction system using FastAPI backend and Streamlit frontend.

## ✨ Features

- 🤖 **ML Model** - XGBoost classifier trained on German credit data
- 📊 **Explainability** - SHAP values for feature importance
- 🎨 **Interactive UI** - Streamlit web interface
- ⚡ **REST API** - FastAPI backend with full documentation
- 🚀 **Production Ready** - Deployed on Render + Streamlit Cloud (FREE)

## 🚀 Quick Start

### Local Development

```bash
# Build (installs dependencies & trains model if needed)
./build.sh

# Start servers
./start.sh
```

Then open:
- Frontend: http://localhost:8501
- Backend API: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

### Free Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete guide.

**TL;DR:**
1. Push to GitHub: `git push origin main`
2. Deploy on Render (3-5 min)
3. Deploy on Streamlit Cloud (2 min)
4. Done! ✅

## 📁 Project Structure

```
.
├── backend/                          # FastAPI backend
│   ├── main.py                      # API endpoints
│   ├── train_model.py               # Model training script
│   ├── models/                      # Trained model (pre-committed)
│   │   └── xgb_credit_pipeline.pkl  # XGBoost pipeline
│   ├── german_credit_data.csv       # Training data
│   └── requirements.txt             # Backend dependencies
│
├── frontend/                         # Streamlit frontend
│   ├── streamlit_app.py             # UI
│   ├── requirements.txt             # Frontend dependencies
│   └── .streamlit/                  # Streamlit config
│
├── build.sh                         # Build script
├── start.sh                         # Start servers
├── deploy.sh                        # Git deployment helper
├── DEPLOYMENT.md                    # Deployment guide
├── DEPLOY_QUICK.md                  # Quick reference
└── README.md                        # This file
```

## 🛠️ Tech Stack

**Backend:**
- FastAPI
- XGBoost
- SHAP (explainability)
- Joblib (model serialization)

**Frontend:**
- Streamlit
- Requests

**Deployment:**
- Render (Backend)
- Streamlit Cloud (Frontend)

## 📊 Model Details

- **Algorithm:** XGBoost Classifier
- **Training Data:** German Credit Dataset (1000 samples)
- **Features:** Age, Sex, Job, Housing, Savings, Checking, Credit Amount, Duration, Purpose
- **Performance:** High accuracy & explainability

## 🚀 Deployment URLs

Once deployed:
- **API**: https://credit-risk-backend-xxxx.onrender.com
- **Frontend**: https://yourapp.streamlit.app

## 💰 Cost

Completely FREE! 🎉

- Render Free: 750 hrs/month
- Streamlit Cloud: Unlimited
- **Total: $0/month**

## 📝 API Example

```bash
curl -X POST https://your-backend.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 30,
    "sex": "male",
    "job": "skilled",
    "housing": "rent",
    "saving_accounts": "moderate",
    "checking_account": "little",
    "credit_amount": 5000,
    "duration": 24,
    "purpose": "car"
  }'
```

Response:
```json
{
  "success": true,
  "prediction": 1,
  "features": {...},
  "shap_values": [...]
}
```

## 🐛 Troubleshooting

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed troubleshooting.

**Quick checks:**
```bash
# Test backend locally
curl http://localhost:8000/health

# Test in production
curl https://your-backend.onrender.com/health

# API documentation
http://localhost:8000/docs
https://your-backend.onrender.com/docs
```

## 📚 Documentation

- [Deployment Guide](DEPLOYMENT.md) - Complete setup & troubleshooting
- [Quick Reference](DEPLOY_QUICK.md) - Fast deployment checklist
- [FastAPI Docs](http://localhost:8000/docs) - Interactive API documentation

## 👨‍💻 Development

To retrain the model:

```bash
cd backend
python train_model.py
git add models/xgb_credit_pipeline.pkl
git commit -m "Retrain model"
git push
```

## 📄 License

MIT

## 🎯 Next Steps

1. ✅ Clone the repo
2. ✅ Run `./build.sh`
3. ✅ Run `./start.sh`
4. ✅ Deploy to Render + Streamlit Cloud (see [DEPLOYMENT.md](DEPLOYMENT.md))
5. ✅ Share with the world!

---

**Built with ❤️ for credit risk prediction**
