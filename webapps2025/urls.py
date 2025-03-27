"""
URL configuration for webapps2025 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Function to redirect root URL to /home/
def redirect_to_home(request):
    return redirect('home')


urlpatterns = [
    path('', redirect_to_home, name='root_redirect'),  # Redirect root to home
    path('admin/', admin.site.urls),  # Admin dashboard URL
    path('', include('register.urls')),  # Include register URLs at the root level
    path('register/', include('register.urls')),  # Include register app URLs
    path('payapp/', include('payapp.urls')),  # Payapp URLs
    path('currency/', include('currency_api.urls')),  # Currency API URLs
]
