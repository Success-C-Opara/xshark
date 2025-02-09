# website/urls.py
from django.urls import path
# from .views import submit_page_data
from . import views




# website/urls.py
# from django.urls import path

urlpatterns = [
     path('site/<str:site_name>/', views.view_site, name='view_site'),


    
]




