from django.db import models
from django.conf import settings
from ..asset.models import Asset

# Create your models here.


class InventorySession(models.Model):
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    manager = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, null = True, blank= True)
    def __str__(self):
        rtn = "Date de début: " + self.startDate
        rtn += "Date de fin: " + self.endDate
        rtn += "Manager: " + self.manager


class InventoryItem(models.Model):
    inventorySession = models.ForeignKey(InventorySession, on_delete=models.SET_NULL, null=True)
    asset = models.ForeignKey(Asset, on_delete=models.SET_NULL, null=True)
    inventorist = models.ForeignKey(settings.AUTH_USER_MODEL,
      on_delete=models.SET_NULL, null = True, blank= True)
    date = models.DateTimeField()
    comment = models.TextField(max_length=1500, null=True)    

    class Status(models.TextChoices):
        OK = 'Ok'
        NON_FUNCTIONAL = "HS"
        LOOSE = 'Lost'

    status = models.CharField(max_length=150,
        choices=Status.choices,
        default=Status.OK,
    )
    
    
class Inventory(models.Model):
    inventorySession = models.ForeignKey(InventorySession, on_delete=models.SET_NULL, null=True)
    inventoryItem = models.ForeignKey(InventoryItem, on_delete=models.SET_NULL, null=True)
