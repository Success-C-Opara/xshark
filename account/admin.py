from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.


from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'password')  # Show these fields in the admin panel


