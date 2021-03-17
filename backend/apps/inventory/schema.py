import graphene
from graphene_django import DjangoObjectType

from .models import Inventory


class InventoryType(DjangoObjectType):
    class Meta:
        model = Inventory


class Query(graphene.ObjectType):
    inventories = graphene.List(InventoryType)

    def resolve_inventories(self, info, **kwargs):
        return Inventory.objects.all()