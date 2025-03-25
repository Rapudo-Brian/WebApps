from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'currency', 'balance', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('currency', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)

