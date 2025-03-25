from django.urls import path
from .views import dashboard, send_money, request_money, manage_requests
from .api import currency_conversion
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('send_money/', send_money, name='send_money'),
    path('request_money/', request_money, name='request_money'),
    path('manage_requests/', manage_requests, name='manage_requests'),
    path('conversion/<str:currency1>/<str:currency2>/<str:amount>/', currency_conversion, name='conversion'),
]
