from django.db import models
from django.conf import settings
from apps.asset.models import Asset


class InventorySession(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    manager = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.start_date


class InventoryItem(models.Model):

    class Statuts(models.TextChoices):
        OK = 'OK', 'Ok'
        NON_FUNCTIONTAL = 'HS',  'NON_FUNCTIONTAL'
        LOOSE = 'LS', 'LOOSE'

    statuts = models.CharField(
        max_length=2,
        choices=Statuts.choices,
        default=Statuts.OK,
    )

    inventory_session = models.ForeignKey(
        InventorySession, related_name="inventory_sessions", on_delete=models.CASCADE)
    asset = models.ForeignKey(
        Asset, related_name="assets", on_delete=models.CASCADE)
    inventorist = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField()
    comment = models.TextField()

    def __str__(self):
        return self.comment
