import graphene
from graphene_django import DjangoObjectType

from .models import Inventory
from .models import InventorySession
from .models import InventoryItem


class InventorySessionType(DjangoObjectType):
    class Meta:
        model = InventorySession
        
class InventoryItemType(DjangoObjectType):
    class Meta:
        model = InventoryItem

        
class InventoryType(DjangoObjectType):
    class Meta:
        model = Inventory

class Query(graphene.ObjectType):
    inventories = graphene.List(InventoryType)

    def resolve_inventories(self, info, **kwargs):
        return Inventory.objects.all()

# CREATE
class CreateInventoryMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        inventory_session = graphene.ID()
        inventory_item = graphene.ID()

    # The class attributes define the response of the mutation
    inventory = graphene.Field(InventoryType)

    @classmethod
    def mutate(cls, root, info, inventory_session_id, inventory_item_id):
        inventory = Inventory.objects.create(inventory_session_id=inventory_session_id, inventory_item_id=inventory_item_id)

        # Notice we return an instance of this mutation
        return CreateInventoryMutation(inventory=inventory)


# UPDATE
class UpdateInventoryMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()
        inventory_session = graphene.ID()
        inventory_item = graphene.ID()

    # The class attributes define the response of the mutation
    inventory = graphene.Field(InventoryType)

    @classmethod
    def mutate(cls, root, info, id, inventory_session_id, inventory_item_id):
        inventory = Inventory.objects.get(pk=id)
        inventory.inventory_session_id = inventory_session_id
        inventory.inventory_item_id = inventory_item_id
        inventory.save()

        # Notice we return an instance of this mutation
        return UpdateInventoryMutation(inventory=inventory)


# DELETE
class DeleteInventoryMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    # The class attributes define the response of the mutation
    deleted = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        deleted = True
        try:
            inventory = Inventory.objects.get(pk=id)
            inventory.delete()
        except Inventory.DoesNotExist:
            deleted = False

        # Notice we return an instance of this mutation
        return DeleteInventoryMutation(deleted=deleted)


# MUTATIONS
class Mutation(graphene.ObjectType):
    create_inventory = CreateInventoryMutation.Field()
    update_inventory = UpdateInventoryMutation.Field()
    delete_inventory = DeleteInventoryMutation.Field()