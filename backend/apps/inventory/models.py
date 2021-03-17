from django.db import models
from django.conf import settings
from apps.asset.models import Asset

# Create your models here.

   class InventorySession(models.Model):
        start_date = models.DateTimeField()
        end_date = models.DateTimeField()
        manager = models.ForeignKey(
            User,  # foreignkey(user)
            on_delete=models.CASCADE,
        )

    class InventoryItem(models.Model):
        InventorySession = models.ForeignKey(
            InventorySession,
            on_delete=models.CASCADE,
        )
        asset = models.ForeignKey(
            Asset,
            on_delete=models.CASCADE,
        )
        inventorist = models.ForeignKey(
            User, # foreignkey(user)
            on_delete=models.CASCADE,
        )
        date = models.DateTimeField()

        class Status(models.TextChoices):
            OK = 'LE', 'Ok'
            NON_FUNCTIONAL = 'Non functionnal',  'Maintenance'
            LOOSE = 'LO', 'Loose'

        comment = models.CharField(max_length=200)
