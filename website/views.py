from django.shortcuts import render, get_object_or_404 ,redirect
from django.http import Http404
from django.utils import timezone
from .models import UserLink
from .models import PageData
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.timezone import now


# def view_site(request, site_name):
#     link_id = request.GET.get('id')

#     if not link_id:
#         raise Http404("Invalid link.")

#     user_link = get_object_or_404(UserLink, link__contains=link_id)

#     # Ensure the link is active and within the correct timeframe
#     if not user_link.is_link_active():
#         raise Http404("This link is inactive or expired.")

#     # Render the correct page based on the site name
#     template_name = f'website/{user_link.site.name.lower()}.html'

#     return render(request, template_name, {'user_link': user_link})



# ---- for submission of user data - from the pages 
# ---- for submission of user data - from the pages 


from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone
from .models import UserLink, PageData

def view_site(request, site_name):
    link_id = request.GET.get('id')

    if not link_id:
        raise Http404("Invalid link.")

    user_link = get_object_or_404(UserLink, link__contains=link_id)

    # Ensure the link is active and within the correct timeframe
    if not user_link.is_link_active():
        raise Http404("This link is inactive or expired.")

    # Handle form submission for product form
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')

        # Check if the name and surname fields are provided
        if name and surname:
            # Manually create the PageData object and save it
            page_data = PageData(
                user_link=user_link,  # Link the PageData to the UserLink
                name=name,            # Store the name submitted via the form
                surname=surname,      # Store the surname submitted via the form
                user=user_link.user,  # Store the user who submitted the form
                page_name=user_link.site.name,  # Store the site name
                link=user_link.link   # Store the exact link used for the page
            )
            # Save the PageData instance manually
            page_data.save()

        # After saving, redirect back to the same page (same link)
        return redirect(request.get_full_path())

    # Render the correct page based on the site name
    template_name = f'website/{user_link.site.name.lower()}.html'

    return render(request, template_name, {'user_link': user_link})












