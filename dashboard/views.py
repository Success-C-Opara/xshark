from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from website.models import UserLink, LinkClick
from dashboard.models import Notification

from website.models import PageData






@login_required  # Ensures only logged-in users can access
def dashboard(request):
   
     # Fetch all links tied to the logged-in user
    user_links = UserLink.objects.filter(user=request.user)

       # Fetch notifications for the logged-in user
    notifications = Notification.objects.all().order_by('-created_at')

    # Filter active links only (without deleting inactive links)
    active_links = [link for link in user_links if link.is_link_active()]

    # Organize PageData by site name
    # page_data = {link.site.name: PageData.objects.filter(user_link=link) for link in active_links}
    # page_data = {link.site: PageData.objects.filter(user_link=link) for link in user_links}
    page_data = {
        link.site.name: PageData.objects.filter(user_link=link, user=request.user) 
        for link in active_links
    }

    context = {
        'user': request.user,
        'active_links': active_links,  # Only active links will be displayed
        'page_data': page_data,  # Stores submitted user data per active link
        'notifications': notifications,  # Pass the user's notifications to the template
    }


    return render(request, 'dashboard/index.html', context)










   # dashboard/views.py






def site_view(request, site_name):
    # Retrieve the link object for the specific user and site
    user_link = get_object_or_404(UserLink, user=request.user, site__name=site_name)

    if user_link.is_link_active():  # Check if the link is active
        # Retrieve or create a LinkClick instance for this specific user_link
        link_click, created = LinkClick.objects.get_or_create(user_link=user_link)

        # Increment the click count (this tracks how many times the link has been clicked)
        link_click.increment_click()

        # Redirect to the actual URL
        return redirect(user_link.link)
    else:
        # If the link is inactive, show an error page
        return render(request, 'error_page.html')














   
   
