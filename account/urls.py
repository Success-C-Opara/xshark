
from django.contrib import admin
from django.urls import path
from account import views  # Import views from the account app


urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),

]