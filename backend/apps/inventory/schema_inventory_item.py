import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from .models import Inventory
from .models import InventorySession
from .models import InventoryItem

class InventoryItemType(DjangoObjectType):
    class Meta:
        model = InventoryItem


class Query(graphene.ObjectType):
    Inventory_items = graphene.List(InventoryItemType)

    def resolve_Inventory_items(self, info, **kwargs):
        return InventoryItemType.objects.all()

# CREATE
class CreateInventoryItemMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        inventory_session_id = graphene.ID()
        asset_id = graphene.ID()
        inventorist_id = graphene.ID()
        date = graphene.Date()
        status = graphene.String()
        comment = graphene.String()

    # The class attributes define the response of the mutation
    inventory_session = graphene.Field(InventoryItemType)

    @classmethod
    def mutate(cls, root, info, Inventory_item_id, asset_id, inventorist_id, date, status, comment):
        inventory_item = InventoryItem.objects.create(Inventory_session_id=Inventory_session_id, asset_id=asset_id, inventorist_id=inventorist_id, date=date, status=status, comment=comment)

        # Notice we return an instance of this mutation
        return CreateInventoryItemMutation(inventory_item=inventory_item)


# UPDATE
class UpdateInventoryItemMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()
        inventory_session_id = graphene.ID()
        asset = graphene.ID()
        inventorist_id = graphene.ID()
        date = graphene.Date()
        status = graphene.String()
        comment = graphene.String()

    # The class attributes define the response of the mutation
    inventory_session = graphene.Field(InventoryItemType)

    @classmethod
    def mutate(cls, root, info, id, Inventory_session_id, asset_id, inventorist_id, date, status, comment):
        Inventory_item = InventoryItem.objects.get(pk=id)
        Inventory_item.Inventory_session_id = Inventory_session_id
        Inventory_item.asset_id = asset_id
        Inventory_item.inventorist_id = inventorist_id
        Inventory_item.date = date
        Inventory_item.status = status
        Inventory_item.comment = comment
        Inventory_item.save()

        # Notice we return an instance of this mutation
        return UpdateInventoryMutation(Inventory_item=Inventory_item)


# DELETE
class DeleteInventoryItemMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    # The class attributes define the response of the mutation
    deleted = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        deleted = True
        try:
            Inventory_item = InventoryItem.objects.get(pk=id)
            Inventory_item.delete()
        except InventoryItem.DoesNotExist:
            deleted = False

        # Notice we return an instance of this mutation
        return DeleteInventoryItemMutation(deleted=deleted)


# MUTATIONS
class Mutation(graphene.ObjectType):
    create_Inventory_item = CreateInventoryItemMutation.Field()
    update_Inventory_item = UpdateInventoryItemMutation.Field()
    delete_Inventory_item = DeleteInventoryItemMutation.Field()