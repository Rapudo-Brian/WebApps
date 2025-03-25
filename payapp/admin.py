from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'amount', 'status', 'timestamp')
    search_fields = ('sender__username', 'receiver__username')
    list_filter = ('status', 'timestamp')

admin.site.register(Transaction, TransactionAdmin)

