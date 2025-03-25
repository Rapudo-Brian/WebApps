from django.urls import path
from .views import convert_currency

urlpatterns = [
    path('conversion/<str:currency1>/<str:currency2>/<str:amount>/', convert_currency, name='convert_currency'),
]
