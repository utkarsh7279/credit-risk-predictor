#!/bin/bash
# Quick deployment helper script

echo "🚀 Credit Risk Predictor - Deployment Helper"
echo "=============================================="
echo ""

# Check if git repo exists
if [ ! -d .git ]; then
    echo "❌ Not a git repository. Initializing..."
    git init
    git branch -M main
    echo "✅ Git initialized"
fi

# Show status
echo "📊 Current git status:"
git status --short
echo ""

# Add all files
echo "📦 Adding files to git..."
git add .
echo "✅ Files staged"
echo ""

# Show what will be committed
echo "📝 Files ready to commit:"
git status --short
echo ""

# Commit
read -p "Enter commit message (or press Enter for default): " commit_msg
if [ -z "$commit_msg" ]; then
    commit_msg="Prepare for deployment with Render + Streamlit Cloud"
fi

git commit -m "$commit_msg"
echo "✅ Changes committed"
echo ""

# Check for remote
if git remote | grep -q origin; then
    echo "📡 Pushing to GitHub..."
    git push origin main
    echo "✅ Pushed to GitHub"
else
    echo "⚠️  No remote 'origin' found"
    echo ""
    echo "To push to GitHub:"
    echo "1. Create a new repo on GitHub"
    echo "2. Run: git remote add origin https://github.com/yourusername/your-repo.git"
    echo "3. Run: git push -u origin main"
fi

echo ""
echo "🎉 Next steps:"
echo "1. Deploy backend on Render: https://render.com"
echo "2. Deploy frontend on Streamlit Cloud: https://share.streamlit.io"
echo ""
echo "📖 See DEPLOYMENT.md for detailed instructions"
