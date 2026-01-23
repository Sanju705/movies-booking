"""
Google Gemini AI Service for Movie Booking Chatbot
Handles all AI-powered responses
"""

import google.generativeai as genai
from django.conf import settings


class GeminiChatbot:
    def __init__(self):
        """Initialize Gemini AI with API key"""
        api_key = getattr(settings, 'GEMINI_API_KEY', None)
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in settings.py")
        
        genai.configure(api_key=api_key)
        # Use the latest available Gemini model
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        self.chat_history = []
    
    def get_response(self, user_message: str) -> str:
        """
        Get AI response from Gemini for user message
        Maintains conversation context
        """
        try:
            # Add user message to history
            self.chat_history.append({
                "role": "user",
                "parts": [user_message]
            })
            
            # Create the prompt with movie booking context
            system_prompt = """You are a helpful movie booking assistant chatbot for a cinema. 
            You help users with:
            - Movie recommendations
            - Booking information and process
            - Show timings and dates
            - Pricing details
            - Payment methods (Razorpay)
            - Ticket cancellation and refund policies
            - General cinema FAQs
            
            Keep responses concise, friendly, and relevant to movie booking.
            If asked about something unrelated to movies/cinema, politely redirect to movie booking topics."""
            
            # Generate response
            response = self.model.generate_content(
                system_prompt + "\n\nUser: " + user_message,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=500,
                )
            )
            
            ai_response = response.text
            
            # Add AI response to history
            self.chat_history.append({
                "role": "model",
                "parts": [ai_response]
            })
            
            return ai_response
            
        except Exception as e:
            error_str = str(e)
            print(f"Error getting AI response: {error_str}")
            
            # Handle specific quota/rate limit errors
            if "429" in error_str or "quota" in error_str.lower():
                return """⏸️ API quota exceeded! The free tier has a daily limit.

**Solutions:**
1. **Wait until tomorrow** - Quota resets daily
2. **Upgrade to paid plan** - Get higher limits at https://console.cloud.google.com/billing
3. **Check your quota** - https://ai.dev/rate-limit

For now, please try again tomorrow or contact support."""
            
            elif "401" in error_str or "unauthenticated" in error_str.lower():
                return "❌ Authentication failed! Please check your API key in settings.py"
            
            elif "404" in error_str or "not found" in error_str.lower():
                return "❌ Model not found! Please update the model name in gemini_service.py"
            
            else:
                return f"⚠️ Having trouble connecting to AI: {error_str[:100]}... Please try again later."
    
    
    def clear_history(self):
        """Clear chat history for new conversation"""
        self.chat_history = []


# Global chatbot instance
chatbot = GeminiChatbot()
