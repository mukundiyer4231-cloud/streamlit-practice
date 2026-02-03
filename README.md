# 💕 Valentine's Week App 💕

A beautiful, animated Streamlit app that changes daily during Valentine's week (Feb 7-14), showing personalized messages and unique themes for each special day!

## ✨ Features

| Day | Date | Theme |
|-----|------|-------|
| 🌹 Rose Day | Feb 7 | Pink background with animated pixelated roses |
| 💍 Propose Day | Feb 8 | Interactive Yes/No buttons (No button moves!) |
| 🍫 Chocolate Day | Feb 9 | Custom PNG image display |
| 🧸 Teddy Day | Feb 10 | Custom PNG image display |
| 🤞 Promise Day | Feb 11 | Custom PNG image display |
| 🤗 Hug Day | Feb 12 | Custom PNG image display |
| 💋 Kiss Day | Feb 13 | Custom PNG image display |
| ❤️ Valentine's Day | Feb 14 | Animated pixelated hearts |

## 🚀 Setup Instructions

### 1. Add Your Custom Messages
Edit `messages.py` and fill in your personalized messages for each day:
```python
ROSE_DAY = """Your special Rose Day message here..."""
PROPOSE_DAY = """Your proposal message here..."""
# ... and so on
```

### 2. Add Your Images
Place your PNG images in the `assets/` folder:
- `assets/chocolate.png` - for Chocolate Day
- `assets/teddy.png` - for Teddy Day
- `assets/promise.png` - for Promise Day
- `assets/hug.png` - for Hug Day
- `assets/kiss.png` - for Kiss Day

### 3. Test Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

### 4. Preview Different Days
Use the sidebar (click the `>` arrow on the left) to preview how each day will look!

## 🌐 FREE Deployment on Streamlit Cloud

### Step 1: Create a GitHub Repository
1. Go to [github.com](https://github.com) and sign in (or create a free account)
2. Click "New Repository"
3. Name it something like `valentine-app`
4. Make it **Public** (required for free Streamlit hosting)
5. Upload all your files:
   - `app.py`
   - `messages.py`
   - `requirements.txt`
   - `assets/` folder with your images

### Step 2: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository
5. Set the main file path to `app.py`
6. Click "Deploy!"

### Step 3: Share the Link! 💝
Your app will be live at: `https://your-app-name.streamlit.app`

Share this link with your partner and watch them smile! 😊

## 📁 Project Structure
```
valentine-app/
├── app.py              # Main application
├── messages.py         # Your custom messages (EDIT THIS!)
├── requirements.txt    # Dependencies
├── README.md           # This file
└── assets/             # Your images go here
    ├── chocolate.png
    ├── teddy.png
    ├── promise.png
    ├── hug.png
    └── kiss.png
```

## 💡 Tips

- **Preview Mode**: Use the sidebar to test how each day will look before the actual date
- **Image Size**: Keep images under 1MB for best performance
- **Messages**: Use `\n` for line breaks in your messages if needed

---

Made with 💕 for your special someone!
