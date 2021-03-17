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
        name = graphene.String(required=True)

    # The class attributes define the response of the mutation
    organization = graphene.Field(InventoryType)

    @classmethod
    def mutate(cls, root, info, inventorySession, inventoryItem ):
        organization = Inventory.objects.create(name=name)

        # Notice we return an instance of this mutation
        return CreateInventoryMutation(organization=organization)

#update

#delete



#InventorySession






#InventoryItem