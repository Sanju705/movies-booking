# 🚀 INSTALLATION GUIDE - Gemini AI Chatbot

## Step 1: Get Gemini API Key (2 minutes)
1. Go to: https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy your key

## Step 2: Install Python Packages (3 minutes)
```bash
pip install -r requirements.txt
```

## Step 3: Configure Settings (1 minute)

### Option A: Simple (for development only)
Edit `moviesbooking/settings.py`:
```python
GEMINI_API_KEY = "paste_your_key_here"
```

### Option B: Secure (using environment variables)
1. Rename `.env.example` to `.env`
2. Edit `.env` and add your API key:
   ```
   GEMINI_API_KEY=paste_your_key_here
   ```
3. Update `moviesbooking/settings.py`:
   ```python
   import os
   from dotenv import load_dotenv
   load_dotenv()
   GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
   ```

## Step 4: Run Server
```bash
python manage.py runserver
```

## Step 5: Access Chatbot
Open your browser: **http://localhost:8000/chatbot/**

---

## ✅ What Gets Installed

| Component | Purpose |
|-----------|---------|
| `gemini_service.py` | AI integration & conversation logic |
| `api_views.py` | Chat API endpoints |
| `chatbot.js` | Frontend chat interface |
| `chatbot.html` | Chatbot HTML template |
| Updated `urls.py` | New routes for chatbot |
| Updated `settings.py` | API key configuration |

---

## 📍 File Locations

```
moviesbooking/
├── app/
│   ├── gemini_service.py      ← AI Service
│   ├── api_views.py           ← API Endpoints
│   ├── urls.py                ← Updated Routes
│   ├── views.py               ← Updated Views
│   └── templates/
│       └── (old files)
├── templates/
│   ├── chatbot.html           ← Chatbot UI
│   └── (other templates)
├── static/
│   └── chatbot.js             ← Frontend JS
├── moviesbooking/
│   └── settings.py            ← Updated Config
├── GEMINI_SETUP.md            ← Full Documentation
├── .env.example               ← Environment Template
└── requirements.txt           ← Python Dependencies
```

---

## 🧪 Test It Out

1. Visit: http://localhost:8000/chatbot/
2. Try asking:
   - "What movies do you have?"
   - "How much are tickets?"
   - "When are showtimes?"
   - "How do I book tickets?"

---

## ❌ Troubleshooting

### Error: "Module 'google.generativeai' not found"
```bash
pip install google-generativeai
```

### Error: "GEMINI_API_KEY not found in settings"
→ Make sure you've added `GEMINI_API_KEY` to `settings.py`

### Chat messages not sending
→ Press F12, check the console for errors
→ Make sure the API key is valid

### Page shows blank chat
→ Check browser console (F12) for JavaScript errors
→ Ensure `chatbot.js` is loading from `/static/chatbot.js`

---

## 🔒 Security Notes

⚠️ **BEFORE DEPLOYING TO PRODUCTION:**
- [ ] Move API key to environment variables
- [ ] Set `DEBUG = False` in settings
- [ ] Add `ALLOWED_HOSTS` in settings
- [ ] Use HTTPS only
- [ ] Use stronger Django SECRET_KEY

---

## 📞 Support

- Gemini API Issues: https://ai.google.dev/docs/
- Django Issues: https://docs.djangoproject.com/
- Python Packages: https://pip.pypa.io/

---

**You're all set! Your AI chatbot is ready to go.** 🎉
