from django.contrib import admin
from .models import SendBack


@admin.register(SendBack)
class SendBackAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email', 'reason', 'order_number')