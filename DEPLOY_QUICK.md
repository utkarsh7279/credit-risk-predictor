# ⚡ Quick Deployment Checklist

## ✅ Pre-Deployment Checklist

- [x] Backend has CORS enabled
- [x] Frontend uses environment variables for backend URL  
- [x] Model training script included
- [x] Requirements files updated
- [x] Deployment configs created
- [x] Git repository ready

---

## 🚀 Deployment Steps (5 minutes)

### 1️⃣ Push to GitHub (2 min)
```bash
./deploy.sh
# OR manually:
git add .
git commit -m "Deploy config"
git push origin main
```

### 2️⃣ Deploy Backend on Render (2 min setup)
1. Go to https://render.com → Login with GitHub
2. **New +** → **Web Service**
3. Connect repo → Select `credit-risk-predictor`
4. Settings:
   - Name: `credit-risk-backend`
   - Root: `backend`
   - Build: `pip install -r requirements.txt && python train_model.py`
   - Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. **Deploy** (wait 5-10 min)
6. **Copy URL**: `https://credit-risk-backend-xxxx.onrender.com`

### 3️⃣ Deploy Frontend on Streamlit (1 min setup)
1. Go to https://share.streamlit.io → Login with GitHub
2. **New app** → Select repo
3. Main file: `frontend/streamlit_app.py`
4. **Advanced Settings** → Add secret:
   ```toml
   BACKEND_URL = "https://credit-risk-backend-xxxx.onrender.com/predict"
   ```
5. **Deploy** (wait 2-3 min)

---

## 🧪 Test Deployment

1. Open Streamlit app URL
2. Fill credit form
3. Click "Predict Risk"
4. ✅ Should see prediction + SHAP values

---

## 📱 Your Live URLs

**Backend API:**
- Docs: `https://your-backend.onrender.com/docs`
- Health: `https://your-backend.onrender.com/predict` (POST)

**Frontend App:**
- `https://yourapp.streamlit.app`

---

## 🔧 Update Deployment

Just push to GitHub:
```bash
git add .
git commit -m "Update feature"
git push
```
- Render: Auto-deploys in ~5 min
- Streamlit: Auto-deploys in ~2 min

---

## 💰 Cost: $0/month

Both services are 100% FREE! ✅

---

## ⚠️ Common Issues

**Render backend won't start:**
- Check logs for errors
- Verify `train_model.py` runs successfully
- Model file should be created during build

**Frontend can't connect:**
- Verify `BACKEND_URL` in Streamlit secrets
- Check backend is running (visit `/docs`)
- Wait if backend is waking from sleep (~30s)

**CORS errors:**
- Already handled in `backend/main.py`
- If persists, check Render logs

---

## 📞 Support

- **Render:** https://render.com/docs
- **Streamlit:** https://docs.streamlit.io/streamlit-community-cloud
- **GitHub Issues:** Create issue in your repo
