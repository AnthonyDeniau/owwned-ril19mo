import graphene
from graphene_django import DjangoObjectType

from .models import Inventory


#Inventory

class InventoryType(DjangoObjectType):
    class Meta:
        model = Inventory

class QueryInventory(graphene.ObjectType):
    inventories = graphene.List(InventoryType)
    def resolve_inventories(self, info, **kwargs):
        return Inventory.objects.all()

#create
class CreateInventoryMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        inventory_session_id = graphene.ID()
        inventory_item_id = graphene.ID()

    # The class attributes define the response of the mutation
    inventories = graphene.Field(InventoryType)

    @classmethod
    def mutate(cls, root, info, inventory_session_id, inventory_item_id ):
        inventories = Inventory.objects.create(inventory_session_id=inventory_session_id, inventory_item_id=inventory_item_id)

        # Notice we return an instance of this mutation
        return CreateInventoryMutation(inventories=inventories)

#update
class UpdateInventoryMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()
        inventory_session_id = graphene.ID()
        inventory_item_id = graphene.ID()


    # The class attributes define the response of the mutation
    inventories = graphene.Field(InventoryType)

    @classmethod
    def mutate(cls, root, info, id, inventory_session_id, inventory_item_id):
        inventories = Inventory.objects.get(pk=id)
        inventories.inventory_session_id = inventory_session_id
        inventories.inventory_item_id = inventory_item_id
        inventories.save()

        # Notice we return an instance of this mutation
        return UpdateInventoryMutation(inventories=inventories)

#delete
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
            inventories = Inventory.objects.get(pk=id)
            inventories.delete()
        except Inventory.DoesNotExist:
            deleted = False

        # Notice we return an instance of this mutation
        return DeleteInventoryMutation(deleted=deleted)


# MUTATIONS
class MutationInventory(graphene.ObjectType):
    create_inventory = CreateInventoryMutation.Field()
    update_inventory = UpdateInventoryMutation.Field()
    delete_inventory = DeleteInventoryMutation.Field()

#InventorySession

class InventorySessionType(DjangoObjectType):
    class Meta:
        model = InventorySession

class QueryInventorySession(graphene.ObjectType):
    inventorySession = graphene.List(InventorySessionType)
    def resolve_inventories(self, info, **kwargs):
        return InventorySession.objects.all()

#create
class CreateInventorySessionMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        start_date = graphene.Datetime()
        end_date = graphene.Datetime()
        manager_id = graphene.ID()

    # The class attributes define the response of the mutation
    inventorySession = graphene.Field(InventorySessionType)

    @classmethod
    def mutate(cls, root, info, start_date, end_date, manager_id):
        inventorySession = InventorySession.objects.create(start_date=start_date, end_date=end_date, manager_id=manager_id)

        # Notice we return an instance of this mutation
        return CreateInventorySessionMutation(inventorySession=inventorySession)

# update
class UpdateInventorySessionMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()
        start_date = graphene.Datetime()
        end_date = graphene.Datetime()
        manager = graphene.ID()

    # The class attributes define the response of the mutation
    inventorySession = graphene.Field(InventorySessionType)

    @classmethod
    def mutate(cls, root, info, id, start_date, end_date, manager = None):
        inventorySession = InventorySession.objects.get(pk=id)
        inventorySession.start_date = start_date
        inventorySession.end_date = end_date
        if not manager: 
            inventorySession.manager = manager
        inventorySession.save()

        # Notice we return an instance of this mutation
        return UpdateInventorySessionMutation(inventorySession=inventorySession)

#delete
class DeleteInventorySessionMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    # The class attributes define the response of the mutation
    deleted = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        deleted = True
        try:
            inventorySession = InventorySession.objects.get(pk=id)
            inventorySession.delete()
        except InventorySession.DoesNotExist:
            deleted = False

        # Notice we return an instance of this mutation
        return DeleteInventorySessionMutation(deleted=deleted)

# MUTATIONS
class Mutation(graphene.ObjectType):
    create_inventorySession = CreateInventorySessionMutation.Field()
    update_inventorySession = UpdateInventorySessionMutation.Field()
    delete_inventorySession = DeleteInventorySessionMutation.Field()


#InventoryItem