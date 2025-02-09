from django.contrib import admin

from .models import Notification

# Register the Notification model in the admin panel
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'account_name', 'account_number', 'created_at')  # Fields to display in the list view
    search_fields = ('user__username', 'message', 'account_name')  # Make it searchable by user, message, and account name
    list_filter = ('created_at',)  # Filter notifications by created_at date
    ordering = ('-created_at',)  # Order by latest notifications first
admin.site.register(Notification)
