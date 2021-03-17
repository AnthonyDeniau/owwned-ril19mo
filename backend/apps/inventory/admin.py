from django.contrib import admin
from .models import InventorySession
from .models import InventoryItem


admin.site.register(InventoryItem)
admin.site.register(InventorySession)
