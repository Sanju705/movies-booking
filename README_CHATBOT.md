# 🎬 Django Movie Booking Chatbot with Google Gemini AI

A fully functional AI-powered chatbot integration for your Django movie booking application using Google Gemini.

## ✨ Features

- 🤖 **Real-time AI Responses** - Powered by Google Gemini Pro
- 💬 **Conversation Context** - Maintains chat history within session
- 🎨 **Beautiful UI** - Modern, responsive design with animations
- 📱 **Mobile Friendly** - Works seamlessly on all devices
- 🔒 **Secure** - CSRF protection, input validation, XSS prevention
- ⚡ **Fast** - Instant responses with typing indicator
- 🎯 **Movie-Focused** - Customized for cinema assistance

## 📁 What's Included

### New Files
- `app/gemini_service.py` - Gemini AI service integration
- `app/api_views.py` - Chat API endpoints
- `templates/chatbot.html` - Chatbot UI with embedded CSS
- `static/chatbot.js` - Frontend JavaScript logic
- `requirements.txt` - Python dependencies
- `.env.example` - Environment variables template
- Documentation files (INSTALLATION.md, GEMINI_SETUP.md, etc.)

### Modified Files
- `app/urls.py` - Added chatbot routes
- `app/views.py` - Added chatbot view
- `moviesbooking/settings.py` - API key configuration

## 🚀 Quick Start (5 Minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Get Gemini API Key
Visit: https://makersuite.google.com/app/apikey

### 3. Configure Django Settings
Edit `moviesbooking/settings.py`:
```python
GEMINI_API_KEY = "your_actual_api_key_here"
```

### 4. Run Server
```bash
python manage.py runserver
```

### 5. Access Chatbot
Open: http://localhost:8000/chatbot/

## 📖 Documentation

- **[QUICK_START.md](QUICK_START.md)** - 5-minute setup guide
- **[INSTALLATION.md](INSTALLATION.md)** - Detailed installation steps
- **[GEMINI_SETUP.md](GEMINI_SETUP.md)** - Complete documentation
- **[ADVANCED_CONFIG.md](ADVANCED_CONFIG.md)** - Advanced configurations
- **[INTEGRATION_SUMMARY.md](INTEGRATION_SUMMARY.md)** - What was changed

## 🧪 Test the Integration

Run the included test script to verify everything:
```bash
python test_gemini_integration.py
```

This will check:
- ✅ API key configuration
- ✅ Gemini API connection
- ✅ Chat response functionality
- ✅ URL routing
- ✅ Template files
- ✅ Required packages

## 🔌 API Endpoints

### Send Message
```bash
POST /api/chat/
Content-Type: application/json

{
    "message": "What movies do you have?"
}
```

Response:
```json
{
    "success": true,
    "response": "We have several great movies...",
    "user_message": "What movies do you have?"
}
```

### Clear Chat History
```bash
POST /api/clear-chat/
```

Response:
```json
{
    "success": true,
    "message": "Chat history cleared"
}
```

## 🎨 Customization

### Change Chatbot Colors
Edit `templates/chatbot.html`, line ~96:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Change AI Personality
Edit `app/gemini_service.py`, line ~29:
```python
system_prompt = """You are a [YOUR PERSONALITY] movie booking assistant..."""
```

### Customize Response Style
Adjust temperature in `app/gemini_service.py`:
```python
temperature=0.7,  # 0=precise, 1=creative
max_output_tokens=500,
```

## 🔐 Security Best Practices

### For Development
```python
GEMINI_API_KEY = "your_key_here"
DEBUG = True
```

### For Production (Recommended)
1. Use environment variables (`.env` file)
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS`
4. Enable HTTPS
5. Use strong `SECRET_KEY`

Example:
```python
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
```

## 📦 Dependencies

- `google-generativeai>=0.3.0` - Gemini AI API
- `Django>=5.0` - Web framework
- `djangorestframework>=3.14.0` - REST utilities
- `python-dotenv>=1.0.0` - Environment variables (optional)

## 🐛 Troubleshooting

### Error: "GEMINI_API_KEY not found"
→ Add to `settings.py`: `GEMINI_API_KEY = "your_key"`

### Error: "google.generativeai not found"
→ Run: `pip install google-generativeai`

### Chat not working?
1. Open browser console (F12)
2. Check for JavaScript errors
3. Verify API key is valid
4. Check network tab for 500 errors

### Styling not showing?
→ Ensure static files are collected: `python manage.py collectstatic`

## 📊 Project Structure

```
moviesbooking/
├── QUICK_START.md              # 5-minute setup
├── INSTALLATION.md             # Installation guide
├── GEMINI_SETUP.md            # Complete docs
├── ADVANCED_CONFIG.md         # Advanced options
├── INTEGRATION_SUMMARY.md     # What changed
├── requirements.txt           # Dependencies
├── .env.example              # Environment template
├── test_gemini_integration.py # Test script
│
├── app/
│   ├── gemini_service.py     # ✨ AI Service
│   ├── api_views.py          # ✨ API Endpoints
│   ├── urls.py               # Modified
│   ├── views.py              # Modified
│   ├── templates/
│   │   └── ... (existing)
│   └── ...
│
├── templates/
│   ├── chatbot.html          # ✨ Chatbot UI
│   ├── base.html
│   └── ... (existing)
│
├── static/
│   ├── chatbot.js            # ✨ Frontend JS
│   └── CSS/
│
└── moviesbooking/
    ├── settings.py           # Modified (API key)
    └── ... (existing)
```

## 🎯 Typical User Workflow

1. User visits chatbot page
2. Sees welcome message from AI
3. Types a question (e.g., "What movies are available?")
4. Message sent to `/api/chat/` endpoint
5. Gemini AI generates response
6. Response displayed with typing animation
7. User can continue conversation or clear history

## 💡 Example Questions Users Can Ask

- "What movies are showing today?"
- "How much do tickets cost?"
- "What are the showtimes?"
- "How do I book tickets?"
- "Can I cancel my booking?"
- "Do you have any horror movies?"
- "Are there group discounts?"
- "What payment methods do you accept?"

## 🚀 Advanced Features

See **ADVANCED_CONFIG.md** for:
- Database message logging
- Custom AI personalities
- Dark mode styling
- Rate limiting
- Analytics integration
- Production deployment settings

## 📞 Support & Resources

- **Gemini API Docs**: https://ai.google.dev/
- **Django Docs**: https://docs.djangoproject.com/
- **Python Docs**: https://docs.python.org/

## 📝 Configuration Options

| Setting | Purpose | Default |
|---------|---------|---------|
| `GEMINI_API_KEY` | Google Gemini API key | Required |
| `temperature` | AI creativity (0-1) | 0.7 |
| `max_output_tokens` | Max response length | 500 |
| `DEBUG` | Django debug mode | False (production) |
| `ALLOWED_HOSTS` | Allowed domains | [] |

## 🔄 Workflow Diagram

```
User Browser
    ↓
HTML Form
    ↓
chatbot.js (JavaScript)
    ↓
API Request (/api/chat/)
    ↓
api_views.py (Django)
    ↓
gemini_service.py (AI Logic)
    ↓
Google Gemini API
    ↓
JSON Response
    ↓
UI Update with Message
```

## ✅ Testing Checklist

- [ ] API key configured in settings
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] Server running: `python manage.py runserver`
- [ ] Can access: http://localhost:8000/chatbot/
- [ ] Can send messages
- [ ] Receive AI responses
- [ ] Clear chat button works
- [ ] Mobile view looks good

## 🎁 Bonus Features You Can Add

1. **Message History Database** - Store conversations
2. **User Analytics** - Track usage patterns
3. **Sentiment Analysis** - Measure user satisfaction
4. **Multi-language Support** - Support multiple languages
5. **Movie Suggestions** - Integrate with movie database
6. **Booking Integration** - Link to actual bookings

## 📜 License

This integration is provided as part of your Django project.

## 🎉 Congratulations!

You now have an AI-powered movie booking chatbot! Enjoy! 🎬✨

---

**Need help?** Start with [QUICK_START.md](QUICK_START.md) or [INSTALLATION.md](INSTALLATION.md)
