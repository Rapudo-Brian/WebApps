from django.urls import path
from .views import register, login_user, logout_user, home  # Import only relevant views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', home, name='home'),
]
