from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Notification(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user
    message = models.TextField()  # Notification message
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the notification is created
    account_name = models.CharField(max_length=255)  # Account name
    account_number = models.CharField(max_length=20)  # Account number

    
