#!/usr/bin/env python
"""
Test script for Gemini AI Chatbot Integration
Run this to verify everything is working correctly
"""

import os
import sys
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviesbooking.settings')
django.setup()

from django.conf import settings
from app.gemini_service import GeminiChatbot

def test_api_key():
    """Test if API key is configured"""
    print("🔑 Testing API Key Configuration...")
    
    api_key = getattr(settings, 'GEMINI_API_KEY', None)
    
    if not api_key:
        print("❌ GEMINI_API_KEY not found in settings.py")
        print("   → Add this to moviesbooking/settings.py:")
        print("   → GEMINI_API_KEY = 'your_key_here'")
        return False
    
    if api_key == "YOUR_GEMINI_API_KEY_HERE":
        print("❌ GEMINI_API_KEY is still the default placeholder")
        print("   → Get a real API key from: https://makersuite.google.com/app/apikey")
        return False
    
    print("✅ API Key found!")
    return True

def test_gemini_connection():
    """Test connection to Gemini API"""
    print("\n📡 Testing Gemini API Connection...")
    
    try:
        chatbot = GeminiChatbot()
        print("✅ Gemini AI initialized successfully!")
        return True
    except Exception as e:
        print(f"❌ Failed to initialize Gemini AI: {str(e)}")
        print("   → Make sure your API key is valid")
        print("   → Check internet connection")
        return False

def test_chat_response():
    """Test getting a response from Gemini"""
    print("\n💬 Testing Chat Response...")
    
    try:
        chatbot = GeminiChatbot()
        response = chatbot.get_response("What's your name?")
        
        if response and len(response) > 0:
            print("✅ Received response from Gemini AI!")
            print(f"   Response preview: {response[:100]}...")
            return True
        else:
            print("❌ Empty response from Gemini AI")
            return False
            
    except Exception as e:
        print(f"❌ Error getting response: {str(e)}")
        return False

def test_urls():
    """Test if URLs are configured"""
    print("\n🔗 Testing URL Configuration...")
    
    from django.urls import reverse, NoReverseMatch
    
    urls_to_test = [
        ('chatbot', 'Chatbot page'),
        ('chat_api', 'Chat API endpoint'),
        ('clear_chat', 'Clear chat endpoint'),
    ]
    
    all_ok = True
    for url_name, description in urls_to_test:
        try:
            reverse(url_name)
            print(f"✅ {description}: /{url_name}/")
        except NoReverseMatch:
            print(f"❌ {description}: NOT FOUND")
            all_ok = False
    
    return all_ok

def test_templates():
    """Test if templates exist"""
    print("\n📄 Testing Template Files...")
    
    base_path = Path(settings.BASE_DIR)
    files_to_check = [
        base_path / 'templates' / 'chatbot.html',
        base_path / 'static' / 'chatbot.js',
        base_path / 'app' / 'gemini_service.py',
        base_path / 'app' / 'api_views.py',
    ]
    
    all_ok = True
    for file_path in files_to_check:
        if file_path.exists():
            print(f"✅ {file_path.relative_to(base_path)}")
        else:
            print(f"❌ {file_path.relative_to(base_path)} - NOT FOUND")
            all_ok = False
    
    return all_ok

def test_imports():
    """Test if all required packages are installed"""
    print("\n📦 Testing Python Imports...")
    
    packages = [
        ('google.generativeai', 'google-generativeai'),
        ('rest_framework', 'djangorestframework'),
        ('razorpay', 'razorpay'),
        ('qrcode', 'qrcode'),
    ]
    
    all_ok = True
    for module_name, package_name in packages:
        try:
            __import__(module_name)
            print(f"✅ {package_name}")
        except ImportError:
            print(f"❌ {package_name} - NOT INSTALLED")
            print(f"   → Run: pip install {package_name}")
            all_ok = False
    
    return all_ok

def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("🧪 GEMINI AI CHATBOT - INTEGRATION TEST")
    print("=" * 60)
    
    tests = [
        ("API Key", test_api_key),
        ("Gemini Connection", test_gemini_connection),
        ("Chat Response", test_chat_response),
        ("URL Configuration", test_urls),
        ("Template Files", test_templates),
        ("Python Packages", test_imports),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} test failed: {str(e)}")
            results[test_name] = False
    
    # Summary
    print("\n" + "=" * 60)
    print("📋 TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    print(f"\n{passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Your chatbot is ready!")
        print("\n📍 Access it at: http://localhost:8000/chatbot/")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        return 1

if __name__ == '__main__':
    exit_code = run_all_tests()
    sys.exit(exit_code)
