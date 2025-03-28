from django.contrib.auth.models import AbstractUser
from django.db import models
from decimal import Decimal
import requests
from django.conf import settings

EXCHANGE_RATES = {
    ('GBP', 'EUR'): Decimal('1.16'),
    ('GBP', 'USD'): Decimal('1.38'),
    ('EUR', 'GBP'): Decimal('0.86'),
    ('EUR', 'USD'): Decimal('1.18'),
    ('USD', 'GBP'): Decimal('0.72'),
    ('USD', 'EUR'): Decimal('0.85'),
}

class CustomUser(AbstractUser):
    CURRENCY_CHOICES = [
        ('GBP', 'British Pound'),
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
    ]

    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='GBP')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('750.00'))

    def convert_currency(self, amount: Decimal, target_currency: str) -> Decimal:
        """Convert an amount from GBP to the selected currency."""
        if target_currency == "GBP":
            return amount  # No conversion needed
        conversion_rate = EXCHANGE_RATES.get(("GBP", target_currency))
        if conversion_rate:
            return round(amount * conversion_rate, 2)
        return amount  # Return the original amount if no conversion rate found

    def __str__(self):
        return f"{self.username} ({self.currency}) - Balance: {self.balance}"
