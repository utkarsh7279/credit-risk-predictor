# 🚀 Free Deployment Guide

## Deploy Credit Risk Predictor (FastAPI + Streamlit)

---

## 📦 Architecture

- **Backend (FastAPI):** Deployed on **Render** (Free)
- **Frontend (Streamlit):** Deployed on **Streamlit Community Cloud** (Free)

---

## 🔧 Step 1: Deploy Backend on Render

### 1.1 Push to GitHub
```bash
git add .
git commit -m "Add deployment configs"
git push origin main
```

### 1.2 Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up with GitHub (Free - No credit card needed)

### 1.3 Deploy Backend
1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Configure:
   - **Name:** `credit-risk-backend`
   - **Root Directory:** `backend`
   - **Environment:** `Python 3`
   - **Build Command:** 
     ```bash
     pip install -r requirements.txt && python train_model.py
     ```
   - **Start Command:** 
     ```bash
     uvicorn main:app --host 0.0.0.0 --port $PORT
     ```
   - **Instance Type:** `Free`

4. Click **"Create Web Service"**
5. Wait 5-10 minutes for deployment
6. **Copy your backend URL:** `https://credit-risk-backend-xxxx.onrender.com`

---

## 🎨 Step 2: Deploy Frontend on Streamlit Community Cloud

### 2.1 Create Streamlit Account
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub (Free - No credit card needed)

### 2.2 Deploy Frontend
1. Click **"New app"**
2. Select your repository
3. Configure:
   - **Main file path:** `frontend/streamlit_app.py`
   - **Python version:** `3.13`
4. Click **"Advanced settings"**
5. Add **Environment Variables** (Secrets):
   ```toml
   BACKEND_URL = "https://credit-risk-backend-xxxx.onrender.com/predict"
   ```
   ⚠️ Replace `xxxx` with your actual Render backend URL!

6. Click **"Deploy!"**
7. Wait 2-3 minutes

---

## ✅ Step 3: Test Your Deployment

1. Open your Streamlit app URL: `https://yourapp.streamlit.app`
2. Fill in the credit application form
3. Click **"Predict Risk"**
4. Verify the prediction works!

---

## 🔄 Auto-Deploy (Optional)

Both services auto-deploy on git push:
```bash
git add .
git commit -m "Update features"
git push origin main
```

- **Render:** Auto-deploys backend (~5 min)
- **Streamlit:** Auto-deploys frontend (~2 min)

---

## ⚠️ Important Notes

### Render Free Tier
- Spins down after 15 min of inactivity
- First request after sleep takes ~30 seconds
- 750 hours/month free (enough for 1 service 24/7)

### Streamlit Community Cloud
- Always-on (no sleep)
- Unlimited apps
- Fast and reliable

---

## 🐛 Troubleshooting

### Backend Issues
1. Check Render logs: Dashboard → Logs
2. Verify model file exists: Build logs should show "Model trained and saved"
3. Test API directly: `https://your-backend.onrender.com/docs`

### Frontend Issues
1. Check backend URL in Streamlit secrets
2. Verify BACKEND_URL environment variable is set
3. Check browser console for CORS errors

### CORS Errors
- Backend already has CORS enabled in `main.py`
- If issues persist, check Render logs

---

## 💡 Cost Optimization

**Current Setup:** 100% FREE ✅

- Render Free: 1 backend service
- Streamlit Cloud: Unlimited frontend apps
- Total monthly cost: **$0**

---

## 📊 Monitoring

### Render Dashboard
- Monitor uptime
- View logs
- Check metrics

### Streamlit Analytics
- View app usage
- Monitor performance
- Check error logs

---

## 🎯 Next Steps

1. ✅ Deploy backend on Render
2. ✅ Deploy frontend on Streamlit Cloud
3. ✅ Test the live app
4. 🎉 Share with the world!

---

**Need Help?** Check the [Render Docs](https://render.com/docs) or [Streamlit Docs](https://docs.streamlit.io/streamlit-community-cloud)
