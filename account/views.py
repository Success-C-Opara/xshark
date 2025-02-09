from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check for empty fields
        if not email or not password or not confirm_password:
            messages.error(request, "All fields are required")
            return redirect('register')

        # Validate email format
        if '@' not in email or '.' not in email:
            messages.error(request, "Invalid email format")
            return redirect('register')

        # Validate password match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # Check if user exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('register')

        # Create new user (using email as username)
        new_user = User.objects.create_user(username=email, email=email, password=password)
        new_user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')  # Redirect to login page

    return render(request, 'account/register.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate using email as username
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)  # Correct login usage
            messages.success(request, "Login successful!")
            return redirect('dashboard')  # Redirect to the dashboard
        else:
            messages.error(request, "Invalid email or password")
            return redirect('login')

    return render(request, 'account/login.html')  # Render login template for GET request





def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')
