"""
API views for Chatbot integration
Handles chat requests and responses
"""

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .gemini_service import GeminiChatbot


# Create a separate chatbot instance for each session if needed
def get_chatbot():
    """Get or create chatbot instance"""
    return GeminiChatbot()


@csrf_exempt
@require_http_methods(["POST"])
def chat_api(request):
    """
    API endpoint for chatbot
    Accepts POST request with user message and returns AI response
    
    Expected JSON body:
    {
        "message": "user's question here"
    }
    """
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return JsonResponse({
                'success': False,
                'error': 'Message cannot be empty'
            }, status=400)
        
        # Get response from Gemini AI
        chatbot = get_chatbot()
        ai_response = chatbot.get_response(user_message)
        
        return JsonResponse({
            'success': True,
            'response': ai_response,
            'user_message': user_message
        })
    
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON format'
        }, status=400)
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def clear_chat(request):
    """Clear chat history"""
    try:
        chatbot = get_chatbot()
        chatbot.clear_history()
        return JsonResponse({
            'success': True,
            'message': 'Chat history cleared'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)
