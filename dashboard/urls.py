# dashboard/urls.py
from django.urls import path
from dashboard import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),  # Ensure this exists
]
