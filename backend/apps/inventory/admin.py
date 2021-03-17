from django.contrib import admin
from .models import InventorySession, InventoryItem


admin.site.register(InventorySession)
admin.site.register(InventoryItem)
