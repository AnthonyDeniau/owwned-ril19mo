from django.contrib import admin
from .models import InventoryItem
from .models import InventorySession

admin.site.register(InventoryItem)

admin.site.register(InventorySession)



