
from django.db import models
from django.conf import settings
from enum import Enum

from apps.asset.models import Asset

# Create your models here.

class Status(models.Model):
    choices = (
        ('OK', 'ok'),
        ('ERROR', 'error')
    )

class InventorySession(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    manager = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, null = True, blank= True)
   
class InventoryItem(models.Model):
    inventory_session = models.ForeignKey(
        InventorySession, on_delete=models.SET_NULL, null=True, blank=True)
    asset = models.ForeignKey(
        Asset, on_delete=models.SET_NULL, null=True, blank=True)
    inventorist = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, null = True, blank= True)
    date = models.DateField()
    status = models.CharField(max_length=5, choices=Status.choices)
    comment = models.TextField()

class Inventory(models.Model):
    inventory_session = models.ForeignKey(
        InventorySession, on_delete=models.SET_NULL, null=True, blank=True)
    inventory_item = models.ForeignKey(
        InventoryItem, on_delete=models.SET_NULL, null=True, blank=True)
    

    