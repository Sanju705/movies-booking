# 🔧 ADVANCED CONFIGURATION & EXAMPLES

## Using Environment Variables (Recommended)

### Step 1: Install python-dotenv
```bash
pip install python-dotenv
```

### Step 2: Create `.env` file
```
GEMINI_API_KEY=AIzaSyBz0BsiZjt3mZtObIxgy5TCIuCzVTwL238
DEBUG=True
SECRET_KEY=your-secret-key
```

### Step 3: Update `settings.py`
```python
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv(BASE_DIR / '.env')

DEBUG = os.getenv('DEBUG', 'False') == 'True'
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-key')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in environment")
```

### Step 4: Add to `.gitignore`
```
.env
*.env
__pycache__/
*.pyc
```

---

## 🧬 Custom Chatbot Configurations

### Movie-Specific Chatbot
Edit `app/gemini_service.py`:

```python
system_prompt = """You are a movie ticket booking assistant for CineMax Theater.

IMPORTANT INFORMATION:
- Ticket Price: ₹300 per ticket
- Operating Hours: 10 AM - 11 PM
- Group Discounts: 10% for groups of 5+
- Payment Methods: Razorpay (UPI, Cards, Wallets)
- Cancellation: Free cancellation up to 2 hours before show

Current Movies:
- Dune: Part Two (Action/Sci-Fi)
- The Zone of Interest (Drama)
- Oppenheimer (Thriller)

Help users with:
1. Movie recommendations based on preferences
2. Booking information
3. Show timings
4. Pricing and discounts
5. Payment methods
6. Cancellation policies

Keep responses concise and helpful. Always recommend calling support for urgent issues."""
```

### Family-Friendly Chatbot
```python
system_prompt = """You are a family-friendly movie assistant!

We offer:
✨ Kid-friendly movies
✨ Family packages
✨ Birthday party bookings
✨ Special events

Help families find perfect movies for their kids!"""
```

### Premium Experience Chatbot
```python
system_prompt = """You are a premium cinema experience advisor.

Premium Features:
🎬 IMAX screens
🎬 Dolby Atmos sound
🎬 VIP lounges
🎬 Premium concessions

Help premium members book their perfect experience."""
```

---

## 📊 Logging Conversations (Optional)

Create `app/models.py` addition:

```python
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user}: {self.message[:50]}"

# Run migrations:
# python manage.py makemigrations
# python manage.py migrate
```

Update `app/api_views.py`:

```python
from .models import ChatMessage

@csrf_exempt
@require_http_methods(["POST"])
def chat_api(request):
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return JsonResponse({'success': False, 'error': 'Message cannot be empty'}, status=400)
        
        chatbot = get_chatbot()
        ai_response = chatbot.get_response(user_message)
        
        # Save to database (optional)
        if request.user.is_authenticated:
            ChatMessage.objects.create(
                user=request.user,
                message=user_message,
                response=ai_response
            )
        
        return JsonResponse({
            'success': True,
            'response': ai_response,
            'user_message': user_message
        })
    
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)
```

---

## 🎨 Custom Styling Theme

### Dark Mode Theme
Add to `templates/chatbot.html` CSS section:

```css
/* Dark Mode */
.chatbot-container {
    background: #1e1e1e;
    color: #e0e0e0;
}

#chat-container {
    background: #2a2a2a;
}

.bot-message {
    background: #3a3a3a;
    color: #e0e0e0;
}

.message-input {
    background: #3a3a3a;
    color: #e0e0e0;
    border-color: #4a4a4a;
}

.message-input:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
}
```

### Compact Mode
```css
.chatbot-container {
    max-width: 500px;
    height: 400px;
}

.message-content {
    max-width: 90%;
    padding: 8px 12px;
    font-size: 13px;
}
```

---

## 🤖 AI Personality Tweaks

### More Creative Responses
```python
response = self.model.generate_content(
    system_prompt + "\n\nUser: " + user_message,
    generation_config=genai.types.GenerationConfig(
        temperature=0.9,  # More creative (0-1)
        max_output_tokens=500,
        top_p=0.95,
        top_k=40,
    )
)
```

### More Precise Responses
```python
response = self.model.generate_content(
    system_prompt + "\n\nUser: " + user_message,
    generation_config=genai.types.GenerationConfig(
        temperature=0.3,  # More precise, less creative
        max_output_tokens=300,
        top_p=0.8,
    )
)
```

---

## 📱 Mobile Optimization

Add to `templates/chatbot.html`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
```

---

## 🔔 Notification Integration

Add browser notifications (optional):

```javascript
// In chatbot.js
async sendMessage() {
    // ... existing code ...
    
    if (data.success) {
        this.displayMessage(data.response, 'bot');
        
        // Notify if page is not focused
        if (!document.hasFocus()) {
            new Notification('Movie Chatbot', {
                body: data.response.substring(0, 50) + '...',
                icon: '/static/cinema-icon.png'
            });
        }
    }
}
```

Request permission:
```javascript
if ('Notification' in window && Notification.permission === 'default') {
    Notification.requestPermission();
}
```

---

## 📈 Analytics Integration

Track chatbot usage:

```javascript
// In chatbot.js
async sendMessage() {
    // ... existing code ...
    
    // Analytics
    if (window.gtag) {
        gtag('event', 'chat_message', {
            message_length: message.length,
            timestamp: new Date().toISOString()
        });
    }
}
```

---

## 🔄 Rate Limiting (Advanced)

Add to `app/api_views.py`:

```python
from django.views.decorators.http import require_http_methods
from django.core.cache import cache
import json

@csrf_exempt
@require_http_methods(["POST"])
def chat_api(request):
    # Rate limit: 10 messages per minute per IP
    client_ip = request.META.get('REMOTE_ADDR')
    cache_key = f'chat_rate_{client_ip}'
    
    request_count = cache.get(cache_key, 0)
    if request_count > 10:
        return JsonResponse({
            'success': False,
            'error': 'Too many requests. Please wait a minute.'
        }, status=429)
    
    cache.set(cache_key, request_count + 1, 60)
    
    # ... rest of the code ...
```

---

## 🚀 Production Deployment

### Settings for Production
```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_SECURITY_POLICY = {
    'default-src': ("'self'",),
}
```

### Environment for Production
```
GEMINI_API_KEY=your-production-key
DEBUG=False
SECRET_KEY=very-secure-random-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@host/dbname
```

---

## 💡 Troubleshooting Advanced Issues

### Slow Responses
- Reduce `max_output_tokens` in generation config
- Use lower `temperature` for faster responses
- Check API quota at: https://console.cloud.google.com/

### Memory Issues
- Clear chat history periodically
- Limit conversation length
- Implement message pagination

### API Errors
```python
# Add detailed logging
import logging
logger = logging.getLogger(__name__)

try:
    response = self.model.generate_content(...)
except Exception as e:
    logger.error(f"Gemini API error: {str(e)}")
    raise
```

---

**Need help? Check GEMINI_SETUP.md for more info!**
