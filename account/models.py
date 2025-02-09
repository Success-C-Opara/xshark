from django.db import models
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)  # Ensures email is unique
    password = models.CharField(max_length=255)  # Store password (should be hashed in practice)

    def __str__(self):
        return self.user.username  # Display the username in the admin panel


