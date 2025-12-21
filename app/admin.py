# app/admin.py
from django.contrib import admin
from .models import ticket

@admin.register(ticket)
class TicketAdmin(admin.ModelAdmin):
    # Display these columns in the list view
    list_display = ['movie_name', 'date', 'showtime', 'ticket']
    
    # ✅ FIX: Add list_display_links to resolve admin.E124 error
    list_display_links = ['movie_name']
    
    # Add filters in the sidebar
    list_filter = ['date', 'movie_name']
    
    # Enable search by movie name
    search_fields = ['movie_name']
    
    # Make these fields editable directly from the list view (movie_name is now safe)
    list_editable = ['date', 'showtime']  # ✅ Removed 'movie_name' from editable
    
    # Order by newest first
    ordering = ['-date', '-showtime']
    
    # Show these fields as readonly (for audit trail)
    readonly_fields = ['ticket']
    
    # Customize field display names
    fieldsets = (
        ('Ticket Info', {
            'fields': ('movie_name', 'date', 'showtime')
        }),
        ('System Info', {
            'fields': ('ticket',),
            'classes': ('collapse',)
        }),
    )
    
    # Customize the admin interface
    list_per_page = 25
    
    # Date hierarchy for easy navigation
    date_hierarchy = 'date'
