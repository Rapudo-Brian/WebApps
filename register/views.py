import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm
from django.core.mail import send_mail  # Import for email verification (future improvement)
from django.contrib.auth.models import update_last_login
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

# Base currency and initial balance
BASE_CURRENCY = "GBP"
INITIAL_AMOUNT = 750


# Fetch converted balance using the Currency Conversion API
def get_converted_amount(currency):
    if currency == BASE_CURRENCY:
        return INITIAL_AMOUNT
    try:
        response = requests.get(f"{settings.BASE_URL}/api/convert/{BASE_CURRENCY}/{currency}/{INITIAL_AMOUNT}/")
        data = response.json()
        return data.get("converted_amount", INITIAL_AMOUNT)
    except:
        return INITIAL_AMOUNT

    # User Registration View with Secure Authentication


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # Validate password strength
            try:
                validate_password(form.cleaned_data.get("password1"), user)
            except ValidationError as e:
                messages.error(request, e.messages[0])
                return render(request, 'register/register.html', {'form': form})

            user.balance = get_converted_amount(user.currency)
            user.save()
            login(request, user)

            # Send a welcome email (optional, improve security later)
            send_mail(
                "Welcome to PayApp",
                "Thank you for registering. Please verify your email to enable full functionality.",
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=True,
            )

            messages.success(request, "Registration successful. Please verify your email.")
            return redirect('home')
        else:
            messages.error(request, "Registration failed. Please check your input.")
    else:
        form = RegistrationForm()

    return render(request, 'register/register.html', {'form': form})


# Secure Login View with session security
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Update last login time
            update_last_login(None, user)

            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'register/login.html', {'form': form})


# Secure Logout View
@login_required
def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


# Secure Home/Dashboard View
@login_required
def home(request):
    return render(request, 'register/home.html', {'user': request.user})

