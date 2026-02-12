# 🚀 DEPLOYED BACKEND CONFIGURATION

**Your Backend is LIVE!** ✅

## Backend URL
```
https://credit-risk-predictor-7qgj.onrender.com
```

## API Endpoints

### Health Check ✅
```bash
GET https://credit-risk-predictor-7qgj.onrender.com/health
```
Response: `{"status":"healthy","service":"credit-risk-backend"}`

### API Documentation
```
https://credit-risk-predictor-7qgj.onrender.com/docs
```

### Make Predictions
```bash
POST https://credit-risk-predictor-7qgj.onrender.com/predict
Content-Type: application/json

{
  "age": 30,
  "sex": "male",
  "job": "skilled",
  "housing": "rent",
  "saving_accounts": "moderate",
  "checking_account": "little",
  "credit_amount": 5000,
  "duration": 24,
  "purpose": "car"
}
```

---

## 🎯 Frontend Configuration

The Streamlit frontend is now configured to use your deployed backend:

### Local Development
```bash
./start.sh
# Frontend on http://localhost:8501
# Uses deployed backend URL automatically
```

### Streamlit Cloud
1. Go to https://share.streamlit.io → Your App → Settings
2. Click **Secrets**
3. Add:
   ```toml
   BACKEND_URL = "https://credit-risk-predictor-7qgj.onrender.com/predict"
   ```
4. Click **Save**
5. Done! Auto-redeploys in 2 min

---

## ✅ Status

- ✅ Backend deployed on Render
- ✅ Health check working
- ✅ API endpoints accessible
- ✅ Frontend configured
- ✅ All systems GO!

---

## 🧪 Quick Test

Test your live API:

```bash
curl https://credit-risk-predictor-7qgj.onrender.com/health
```

Expected: `{"status":"healthy","service":"credit-risk-backend"}`

---

## 📊 Your Live URLs

| Service | URL |
|---------|-----|
| Backend API | https://credit-risk-predictor-7qgj.onrender.com |
| API Docs | https://credit-risk-predictor-7qgj.onrender.com/docs |
| Health Check | https://credit-risk-predictor-7qgj.onrender.com/health |
| Frontend | https://yourapp.streamlit.app |

---

**Congratulations! Your credit risk predictor is now LIVE!** 🎉
