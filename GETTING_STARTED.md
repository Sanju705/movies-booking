# 🎬 GETTING STARTED - Visual Guide

## Step 1: Install Requirements ⬇️

```bash
pip install -r requirements.txt
```

Expected output:
```
✓ Installing google-generativeai...
✓ Installing djangorestframework...
✓ Already satisfied: razorpay...
✓ Already satisfied: qrcode...
Successfully installed google-generativeai
```

---

## Step 2: Get Your API Key 🔑

1. **Open browser:** https://makersuite.google.com/app/apikey
2. **Click:** "Create API Key"
3. **Copy:** The key shown
4. **Save:** Somewhere safe (you'll need it next)

Example key format:
```
AIzaSyDxR1234567890abcdefghijklmnopqrst
```

⚠️ **Keep this secret!** Don't share it or commit to GitHub.

---

## Step 3: Update Django Settings ⚙️

Open: `moviesbooking/settings.py`

Find this line (around line 163):
```python
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
```

Replace with your actual key:
```python
GEMINI_API_KEY = "AIzaSyDxR1234567890abcdefghijklmnopqrst"
```

Save the file.

---

## Step 4: Run the Server 🚀

Open terminal/command prompt:

```bash
python manage.py runserver
```

Expected output:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

---

## Step 5: Test the Chatbot 💬

1. **Open browser**
2. **Go to:** http://localhost:8000/chatbot/
3. **You should see:**

```
┌─────────────────────────────────┐
│   🎬 Movie Booking Assistant    │
│  Powered by Google Gemini AI    │
├─────────────────────────────────┤
│                                 │
│  👋 Welcome to our Movie...     │
│                                 │
├─────────────────────────────────┤
│ [Type your question here...  ➤] │
│         [ Clear Chat ]          │
└─────────────────────────────────┘
```

4. **Try asking:**
   - "What movies do you have?"
   - "How much are tickets?"
   - Any movie-related question!

---

## Step 6: Verify Everything Works ✅

Run the test script:

```bash
python test_gemini_integration.py
```

You should see:
```
============================================================
🧪 GEMINI AI CHATBOT - INTEGRATION TEST
============================================================
🔑 Testing API Key Configuration...
✅ API Key found!

📡 Testing Gemini API Connection...
✅ Gemini AI initialized successfully!

💬 Testing Chat Response...
✅ Received response from Gemini AI!
   Response preview: Hello! I'm an AI assistant...

🔗 Testing URL Configuration...
✅ Chatbot page: /chatbot/
✅ Chat API endpoint: /chat_api/
✅ Clear chat endpoint: /clear_chat/

📄 Testing Template Files...
✅ templates/chatbot.html
✅ static/chatbot.js
✅ app/gemini_service.py
✅ app/api_views.py

📦 Testing Python Imports...
✅ google-generativeai
✅ djangorestframework
✅ razorpay
✅ qrcode

============================================================
📋 TEST SUMMARY
============================================================
✅ PASS: API Key
✅ PASS: Gemini Connection
✅ PASS: Chat Response
✅ PASS: URL Configuration
✅ PASS: Template Files
✅ PASS: Python Packages

6/6 tests passed

🎉 All tests passed! Your chatbot is ready!
📍 Access it at: http://localhost:8000/chatbot/
```

---

## 🎯 Common Questions

### Q: Where do I find my messages?
**A:** Messages are stored in browser memory (session). They disappear when you:
- Click "Clear Chat" button
- Close the browser tab
- Log out

### Q: Can I save messages to database?
**A:** Yes! See ADVANCED_CONFIG.md for how to add message logging.

### Q: How do I customize the colors?
**A:** Edit `templates/chatbot.html`, find line ~96, change the gradient colors.

### Q: Is my API key safe?
**A:** No! Move it to `.env` file for production. See ADVANCED_CONFIG.md.

### Q: Can I change the chatbot's personality?
**A:** Yes! Edit `app/gemini_service.py`, line ~29, change `system_prompt`.

### Q: Does it work on mobile?
**A:** Yes! The chatbot is fully responsive.

---

## 🆘 Troubleshooting

### ❌ Error: "GEMINI_API_KEY not found"

**Solution:**
1. Open `moviesbooking/settings.py`
2. Find: `GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"`
3. Replace with actual key
4. Save file
5. Restart server

### ❌ Error: "Module 'google.generativeai' not found"

**Solution:**
```bash
pip install google-generativeai
```

### ❌ Chat page shows blank

**Solution:**
1. Press F12 (open browser console)
2. Check for red errors
3. Make sure `static/chatbot.js` is loading
4. Restart server

### ❌ "Invalid API Key"

**Solution:**
1. Get new key from: https://makersuite.google.com/app/apikey
2. Copy exact key (no spaces)
3. Update settings.py
4. Restart server

### ❌ Chat not responding

**Solution:**
1. Check internet connection
2. Verify API key is valid
3. Check Google quota: https://console.cloud.google.com/
4. Try simpler question first

---

## 📊 Folder Structure

After integration, your project looks like:

```
moviesbooking/
├── 📚 DOCUMENTATION
│   ├── QUICK_START.md           ← You are here!
│   ├── INSTALLATION.md
│   ├── README_CHATBOT.md
│   ├── GEMINI_SETUP.md
│   ├── ADVANCED_CONFIG.md
│   ├── INTEGRATION_SUMMARY.md
│   └── FILE_MANIFEST.md
│
├── ⚙️ CONFIGURATION
│   ├── requirements.txt
│   ├── .env.example
│   └── test_gemini_integration.py
│
├── 🎨 FRONTEND
│   ├── templates/chatbot.html     ← Beautiful UI
│   └── static/chatbot.js          ← Chat logic
│
├── 🧠 BACKEND
│   ├── app/gemini_service.py      ← AI integration
│   ├── app/api_views.py           ← API endpoints
│   ├── app/urls.py                ← Updated routes
│   ├── app/views.py               ← Updated views
│   └── moviesbooking/settings.py  ← Updated config
│
└── 📊 YOUR EXISTING FILES
    ├── app/models.py
    ├── app/forms.py
    ├── templates/ (other)
    └── (all else unchanged)
```

---

## 🎮 Playing with the Chatbot

### Try These Questions:

**About Movies:**
- "What's the best movie for a date night?"
- "Do you have any action movies?"
- "What movies are good for kids?"

**About Bookings:**
- "How do I book tickets?"
- "Can I book group tickets?"
- "How far in advance can I book?"

**About Pricing:**
- "How much are tickets?"
- "Do students get discounts?"
- "What about group rates?"

**About Payment:**
- "What payment methods do you accept?"
- "Can I pay with PayPal?"
- "Is payment secure?"

**About Cancellations:**
- "Can I cancel my booking?"
- "What's your refund policy?"
- "How late can I cancel?"

**Fun Questions:**
- "Who is your favorite actor?"
- "What's your favorite movie?"
- "Can you recommend a movie for me?"

---

## ✨ Next Steps

After everything is working:

1. **Customize:** Change colors, personality, styling
2. **Add Features:** Message logging, analytics, etc.
3. **Deploy:** Move to production with proper security
4. **Integrate:** Link chatbot to real booking system
5. **Monitor:** Track usage and user satisfaction

---

## 📞 Need Help?

1. **Quick Issues?** → Check TROUBLESHOOTING in GEMINI_SETUP.md
2. **Setup Problems?** → Read INSTALLATION.md carefully
3. **Want Customization?** → See ADVANCED_CONFIG.md
4. **API Questions?** → Visit https://ai.google.dev/docs

---

## ✅ You're Ready!

Your AI-powered movie booking chatbot is now:
- ✅ Installed
- ✅ Configured
- ✅ Running
- ✅ Ready to use

**Go impress people with your AI chatbot! 🚀**

Visit: http://localhost:8000/chatbot/

---

**Questions?** → Read the documentation files in your project folder.
