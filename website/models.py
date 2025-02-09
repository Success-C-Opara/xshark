from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


# from website.models import UserLink  # Import the UserLink model

# Site model with no circular reference
class Site(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Define a default function to get the default site (you can adjust the logic)
def get_default_site():
    # You can change the logic to get the default site, like fetching the first Site
    return Site.objects.first()  # Example: returns the first site in the database

# UserLink model with a ForeignKey to Site and a default site
class UserLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=get_default_site)  # Default value function
    link = models.URLField(unique=True, blank=True)  # Auto-generated link
    custom_text = models.CharField(max_length=50, blank=True, help_text="Extra text for the link")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.link:
            unique_id = uuid.uuid4()
            self.link = f"/site/{self.site.name.lower().replace(' ', '-')}/?id={unique_id}"  # Store only relative path
            
            # self.link = f"http://127.0.0.1:8000/site/{self.site.name.lower().replace(' ', '-')}/?id={unique_id}"

        if timezone.now() > self.end_date:
            self.is_active = False  # Auto-deactivate expired links

        super().save(*args, **kwargs)

    def is_link_active(self):
        return self.is_active and self.start_date <= timezone.now() <= self.end_date

    def __str__(self):
        return f"{self.user.username} - {self.site.name} ({'Active' if self.is_active else 'Inactive'})"


# newly added so it will hellp to get any link domail and pass it inside self.link
    def get_full_link(self, request):
        """ Dynamically gets the full URL including the current domain. """
        current_domain = request.get_host()  # Detects the actual domain being used
        scheme = 'https' if request.is_secure() else 'http'  # Check if HTTPS or HTTP
        return f"{scheme}://{current_domain}{self.link}"












class LinkClick(models.Model):
    user_link = models.ForeignKey(UserLink, on_delete=models.CASCADE)
    click_count = models.PositiveIntegerField(default=0)

    def increment_click(self):
        self.click_count += 1
        self.save()

    def __str__(self):
        return f"Link {self.user_link.link} clicked {self.click_count} times"
    


    # to render and submit the data user passes 

  # The model that stores active links

class PageData(models.Model):
    user_link = models.ForeignKey(UserLink, on_delete=models.CASCADE)  # Track which page the data is from
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    # Auto-filled fields from UserLink
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Track which user submitted the data
    page_name = models.CharField(max_length=100 , null=True, blank=True)  # Store the name of the page (site)
    link = models.URLField(null=True, blank=True)
  # Store the exact URL of the page

    def save(self, *args, **kwargs):
        """Automatically fill user, page_name, and link from user_link"""
        if self.user_link:
            self.user = self.user_link.user
            self.page_name = self.user_link.site.name
            self.link = self.user_link.link
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.surname} - {self.page_name}"
