# Create your models here.
from django.db import models
from register.models import CustomUser

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('SEND', 'Sent Payment'),
        ('REQUEST', 'Requested Payment'),
    ]
    sender = models.ForeignKey('register.CustomUser', on_delete=models.CASCADE, related_name='sent_transactions')
    recipient = models.ForeignKey('register.CustomUser', on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('REJECTED', 'Rejected')], default='PENDING')

    def __str__(self):
        return f"{self.sender} -> {self.recipient} ({self.amount} {self.transaction_type})"

