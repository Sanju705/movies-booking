# 🎬 Gemini AI Chatbot Integration for Django Movie Booking

## Quick Start Guide

### 1️⃣ **Get Your Gemini API Key**

1. Visit: https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key and save it securely

### 2️⃣ **Install Required Packages**

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install google-generativeai>=0.3.0
pip install djangorestframework
```

### 3️⃣ **Configure Your Django Settings**

Edit `moviesbooking/settings.py`:

```python
# Add your Gemini API Key
GEMINI_API_KEY = "your_actual_api_key_here"
```

⚠️ **Security Tip:** Use environment variables instead of hardcoding:

```python
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
```

Then create a `.env` file:
```
GEMINI_API_KEY=your_actual_api_key_here
```

### 4️⃣ **Files Created/Modified**

**New Files:**
- `app/gemini_service.py` - Gemini AI integration
- `app/api_views.py` - Chat API endpoints
- `app/templates/chatbot.js` - Frontend JavaScript
- `templates/chatbot.html` - Chatbot UI
- `requirements.txt` - Python dependencies

**Modified Files:**
- `app/urls.py` - Added chatbot routes
- `app/views.py` - Added chatbot view
- `moviesbooking/settings.py` - Added Gemini API key

### 5️⃣ **Run the Server**

```bash
python manage.py runserver
```

Visit: `http://localhost:8000/chatbot/`

---

## 🎯 Features

✅ **Real-time AI Responses** - Powered by Google Gemini  
✅ **Conversation Context** - Maintains chat history  
✅ **Movie Booking Focused** - Customized prompts for cinema assistance  
✅ **Responsive Design** - Works on mobile and desktop  
✅ **Error Handling** - Graceful fallbacks  
✅ **CSRF Protection** - Secure by default  

---

## 📡 API Endpoints

### Send Message
```bash
POST /api/chat/
Content-Type: application/json

{
    "message": "What movies are showing today?"
}
```

**Response:**
```json
{
    "success": true,
    "response": "We have several movies showing today...",
    "user_message": "What movies are showing today?"
}
```

### Clear Chat History
```bash
POST /api/clear-chat/
```

---

## 🎨 Customization

### Modify Chatbot Personality

Edit `app/gemini_service.py`, change the `system_prompt`:

```python
system_prompt = """You are a enthusiastic movie recommendation AI...
Keep responses fun and engaging while providing booking assistance."""
```

### Customize UI Styling

Edit `templates/chatbot.html` - Modify the `<style>` section

### Change Colors

Replace in the gradient:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

---

## 🐛 Troubleshooting

### Error: "GEMINI_API_KEY not found"
→ Check `settings.py` has `GEMINI_API_KEY` configured

### API returns 403 Forbidden
→ Verify your Gemini API key is valid and has quota remaining

### Chat messages not sending
→ Open browser console (F12) and check for errors
→ Ensure `/api/chat/` endpoint is accessible

### CSRF token errors
→ Cookie might be blocked. Check browser settings
→ Verify CSRF middleware is enabled in `settings.py`

---

## 📝 Example Conversation Prompts

- "When can I book tickets?"
- "What's the ticket price?"
- "Do you have any horror movies?"
- "How do I cancel my booking?"
- "What payment methods do you accept?"
- "Are there group discounts?"

---

## 🔐 Security Best Practices

1. **Never commit API keys** - Use environment variables
2. **Keep Django SECRET_KEY secret** - Use `.env`
3. **Validate user input** - Already handled in `api_views.py`
4. **Use HTTPS in production** - Not just HTTP
5. **Set DEBUG = False** - Before deploying

---

## 📚 Additional Resources

- [Google Generative AI Docs](https://ai.google.dev/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Gemini API Pricing](https://ai.google.dev/pricing)

---

## ✨ Next Steps

1. Add chat message persistence to database
2. Implement user-specific chat history
3. Add sentiment analysis for user satisfaction
4. Create admin dashboard for chat analytics
5. Integrate with booking system for real-time info

Enjoy your AI-powered movie booking chatbot! 🎬✨
