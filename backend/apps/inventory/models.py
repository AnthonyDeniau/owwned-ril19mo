from django.db import models
from apps.asset.models import Asset
from django.conf import settings

class InventorySession(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    manager = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.SET_NULL, null=True, blank=True)

    def str(self):
        return self.start_date

class InventoryItem(models.Model):

    class Statuts(models.TextChoices):
        OK = 'OK', 'Ok'
        NON_FUNCTIONTAL = 'NF',  'non functionnal'
        LOOSE = 'LO', 'loose'

    comment = models.TextField()

    
    date = models.DateTimeField()
    
    inventory_session = models.ForeignKey(
        InventorySession, related_name="inventory_sessions", on_delete=models.CASCADE)
    asset = models.ForeignKey(
        Asset, related_name="assets", on_delete=models.CASCADE)
    inventorist = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.SET_NULL, null=True, blank=True)

    statuts = models.CharField(
        max_length=2,
        choices=Statuts.choices,
        default=Statuts.OK,
    )

    def str(self):
        return self.comment

