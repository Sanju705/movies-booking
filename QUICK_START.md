# ⚡ QUICK REFERENCE - Gemini AI Chatbot

## 🎯 In 5 Minutes

```bash
# 1. Install packages
pip install -r requirements.txt

# 2. Get API key
# Visit: https://makersuite.google.com/app/apikey

# 3. Add to settings.py
GEMINI_API_KEY = "your_key_here"

# 4. Run server
python manage.py runserver

# 5. Open browser
# http://localhost:8000/chatbot/
```

---

## 📂 File Reference

| File | Purpose | Action |
|------|---------|--------|
| `app/gemini_service.py` | AI engine | Read only |
| `app/api_views.py` | API endpoints | Read only |
| `templates/chatbot.html` | UI & styles | Edit for colors/layout |
| `static/chatbot.js` | Frontend logic | Edit for behavior |
| `moviesbooking/settings.py` | Config | **Add API key here** |
| `app/urls.py` | Routes | Already updated |
| `app/views.py` | Views | Already updated |

---

## 🔌 API Endpoints

```
POST /api/chat/
  {
    "message": "What movies?"
  }
  → { "success": true, "response": "..." }

POST /api/clear-chat/
  → { "success": true, "message": "Chat cleared" }
```

---

## 🎨 Customize Colors

Edit `templates/chatbot.html` line ~96:

```css
/* Change this line */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* To any colors like */
background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%);
```

Color ideas:
- Purple: `#667eea` to `#764ba2` (current)
- Red: `#FF6B6B` to `#FF1744`
- Green: `#11998E` to `#38EF7D`
- Blue: `#0F2027` to `#203A43`

---

## 🎯 Customize Personality

Edit `app/gemini_service.py` line ~29, change `system_prompt`:

```python
system_prompt = """You are a [YOUR PERSONALITY] movie booking assistant.
[YOUR RULES HERE]
Help users with [YOUR FOCUS]."""
```

Examples:
- "Enthusiastic, witty movie fan"
- "Professional, informative advisor"
- "Casual, friend-like helper"

---

## 🐛 Quick Fixes

| Problem | Solution |
|---------|----------|
| Module not found | `pip install google-generativeai` |
| API key error | Check `GEMINI_API_KEY` in settings.py |
| Chat not sending | Press F12, check console for errors |
| No styling | Ensure `static/chatbot.js` loads |
| Page blank | Check browser console (F12) for errors |

---

## 📍 Access Points

- **Chatbot**: `http://localhost:8000/chatbot/`
- **API**: `http://localhost:8000/api/chat/`
- **Admin**: `http://localhost:8000/admin/`

---

## 📦 What's Installed

```
google-generativeai   ← Gemini API
djangorestframework   ← REST utilities
razorpay             ← Payment (existing)
qrcode               ← Tickets (existing)
python-dotenv        ← Environment vars (optional)
```

---

## 🔒 Security Checklist

```
☐ API key in .env file (not in code)
☐ DEBUG = False in production
☐ ALLOWED_HOSTS set
☐ HTTPS enabled
☐ SECRET_KEY is strong
```

---

## 📊 Project Structure

```
moviesbooking/
├── INSTALLATION.md          ← Setup (read first!)
├── GEMINI_SETUP.md         ← Full docs
├── ADVANCED_CONFIG.md      ← Advanced options
├── INTEGRATION_SUMMARY.md  ← What changed
├── requirements.txt        ← Install these
├── .env.example           ← Copy to .env
│
├── app/
│   ├── gemini_service.py  ← ✨ NEW
│   ├── api_views.py       ← ✨ NEW
│   ├── urls.py            ← Modified
│   └── views.py           ← Modified
│
├── templates/
│   ├── chatbot.html       ← ✨ NEW
│   └── ...
│
└── static/
    ├── chatbot.js         ← ✨ NEW
    └── CSS/
```

---

## 🚀 Next Steps

1. Read `INSTALLATION.md`
2. Get API key from Google
3. Install packages: `pip install -r requirements.txt`
4. Update `settings.py` with API key
5. Run `python manage.py runserver`
6. Visit `http://localhost:8000/chatbot/`
7. Start chatting! 🎉

---

## 💬 Test Messages

Try these to test your chatbot:

- "What movies are playing?"
- "How much are tickets?"
- "When are the showtimes?"
- "Can I get group discounts?"
- "How do I cancel my booking?"
- "What payment methods do you accept?"

---

## 📞 Need Help?

1. Check `GEMINI_SETUP.md` for troubleshooting
2. See `ADVANCED_CONFIG.md` for advanced options
3. Google Gemini Docs: https://ai.google.dev/
4. Django Docs: https://docs.djangoproject.com/

---

## ✨ You're All Set!

Your AI movie booking chatbot is ready to impress! 🎬

Questions? → Read the docs or check the code comments.
