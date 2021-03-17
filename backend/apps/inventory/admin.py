from django.contrib import admin
from .models import InventorySession
from .models import InventoryItem
# Register your models here.
admin.site.register(InventorySession)
admin.site.register(InventoryItem)
