// Movie Booking Chatbot - JavaScript Frontend
// Handles UI and communication with Gemini AI backend

class MovieChatbot {
    constructor() {
        this.chatContainer = document.getElementById('chat-container');
        this.messageInput = document.getElementById('message-input');
        this.sendBtn = document.getElementById('send-btn');
        this.clearBtn = document.getElementById('clear-btn');
        this.apiUrl = '/api/chat/';
        this.clearUrl = '/api/clear-chat/';
        
        this.initializeEventListeners();
    }
    
    initializeEventListeners() {
        this.sendBtn.addEventListener('click', () => this.sendMessage());
        this.clearBtn.addEventListener('click', () => this.clearChat());
        
        // Send message on Enter key
        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });
    }
    
    async sendMessage() {
        const message = this.messageInput.value.trim();
        
        if (!message) {
            alert('Please enter a message');
            return;
        }
        
        // Display user message
        this.displayMessage(message, 'user');
        this.messageInput.value = '';
        
        // Show typing indicator
        this.showTypingIndicator();
        
        try {
            const response = await fetch(this.apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCookie('csrftoken')
                },
                body: JSON.stringify({ message: message })
            });
            
            // Remove typing indicator
            this.removeTypingIndicator();
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            
            if (data.success) {
                // Display AI response
                this.displayMessage(data.response, 'bot');
            } else {
                this.displayMessage(`Error: ${data.error}`, 'error');
            }
            
        } catch (error) {
            this.removeTypingIndicator();
            this.displayMessage(`Error: ${error.message}`, 'error');
            console.error('Error:', error);
        }
        
        // Auto-scroll to bottom
        this.scrollToBottom();
    }
    
    displayMessage(message, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}`;
        
        let html = '';
        if (sender === 'user') {
            html = `<div class="message-content user-message">${this.escapeHtml(message)}</div>`;
        } else if (sender === 'bot') {
            html = `<div class="message-content bot-message">${this.formatBotMessage(message)}</div>`;
        } else if (sender === 'error') {
            html = `<div class="message-content error-message">${this.escapeHtml(message)}</div>`;
        }
        
        messageDiv.innerHTML = html;
        this.chatContainer.appendChild(messageDiv);
        this.scrollToBottom();
    }
    
    formatBotMessage(message) {
        // Convert newlines to <br> and basic markdown-like formatting
        let formatted = this.escapeHtml(message);
        formatted = formatted.replace(/\n/g, '<br>');
        formatted = formatted.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        formatted = formatted.replace(/\*(.*?)\*/g, '<em>$1</em>');
        return formatted;
    }
    
    showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot';
        typingDiv.id = 'typing-indicator';
        typingDiv.innerHTML = '<div class="message-content bot-message"><div class="typing"><span></span><span></span><span></span></div></div>';
        this.chatContainer.appendChild(typingDiv);
        this.scrollToBottom();
    }
    
    removeTypingIndicator() {
        const indicator = document.getElementById('typing-indicator');
        if (indicator) {
            indicator.remove();
        }
    }
    
    async clearChat() {
        if (confirm('Are you sure you want to clear the chat history?')) {
            try {
                const response = await fetch(this.clearUrl, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': this.getCookie('csrftoken')
                    }
                });
                
                const data = await response.json();
                
                if (data.success) {
                    // Clear messages from UI
                    this.chatContainer.innerHTML = '';
                    this.displayMessage('Chat history cleared. How can I help you with movie bookings today?', 'bot');
                }
            } catch (error) {
                console.error('Error clearing chat:', error);
                alert('Failed to clear chat history');
            }
        }
    }
    
    scrollToBottom() {
        this.chatContainer.scrollTop = this.chatContainer.scrollHeight;
    }
    
    escapeHtml(text) {
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, m => map[m]);
    }
    
    getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
}

// Initialize chatbot when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const chatbot = new MovieChatbot();
    // Show welcome message
    chatbot.displayMessage('👋 Welcome to our Movie Booking Assistant! Ask me anything about movies, bookings, showtimes, or our cinema.', 'bot');
});
