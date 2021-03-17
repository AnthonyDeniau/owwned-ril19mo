from django.db import models
from ..asset.models import Asset
from django.conf import settings


class InventorySession(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="inventory_sessions", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return 'Inventaire du %s au %s, manager: %s'% (self.start_date.date(), self.end_date.date(), self.manager.username)


class InventoryItem(models.Model):
    class StatusType(models.TextChoices):
        OK = 'OK', 'Ok'
        NON_FUNCTIONAL = 'NF',  'Non fonctionnel'
        LOST = 'LO', 'Perdu'

    inventory_session = models.ForeignKey(InventorySession, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.SET_NULL, null=True, blank=True)
    inventorist = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="inventory_items", on_delete=models.SET_NULL, null = True, blank= True)
    date = models.DateTimeField()
    status = models.CharField(
        max_length=2,
        choices=StatusType.choices,
        default=StatusType.OK,
    )
    comment = models.TextField()

    def __str__(self):
        return '%s, ajouté le %s par %s' % (self.asset.name, self.date, self.inventory_session.manager.username)