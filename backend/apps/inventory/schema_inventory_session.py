import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from .models import Inventory
from .models import InventorySession
from .models import InventoryItem

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class InventorySessionType(DjangoObjectType):
    class Meta:
        model = InventorySession


class Query(graphene.ObjectType):
    inventory_sessions = graphene.List(InventorySessionType)

    def resolve_inventory_sessions(self, info, **kwargs):
        return InventorySessionType.objects.all()

# CREATE
class CreateInventorySessionMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        start_date = graphene.Date()
        end_date = graphene.Date()
        manager = manager_id = graphene.ID()

    # The class attributes define the response of the mutation
    inventory_session = graphene.Field(InventorySessionType)

    @classmethod
    def mutate(cls, root, info, start_date, end_date, manager_id):
        inventory_session = InventorySession.objects.create(start_date=start_date, end_date=end_date, manager_id=manager_id)

        # Notice we return an instance of this mutation
        return CreateInventorySessionMutation(inventory_session=inventory_session)


# UPDATE
class UpdateInventorySessionMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()
        start_date = graphene.Date()
        end_date = graphene.Date()
        manager = manager_id = graphene.ID()

    # The class attributes define the response of the mutation
    inventory_session = graphene.Field(InventorySessionType)

    @classmethod
    def mutate(cls, root, info, id, start_date, end_date, manager_id):
        inventory_session = InventorySession.objects.get(pk=id)
        inventory_session.start_date = start_date
        inventory_session.end_date = end_date
        inventory_session.manager_id = manager_id
        inventory_session.save()

        # Notice we return an instance of this mutation
        return UpdateInventoryMutation(inventory_session=inventory_session)


# DELETE
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
            inventory_session = InventorySession.objects.get(pk=id)
            inventory_session.delete()
        except InventorySession.DoesNotExist:
            deleted = False

        # Notice we return an instance of this mutation
        return DeleteInventorySessionMutation(deleted=deleted)


# MUTATIONS
class Mutation(graphene.ObjectType):
    create_inventory_session = CreateInventorySessionMutation.Field()
    update_inventory_session = UpdateInventorySessionMutation.Field()
    delete_inventory_session = DeleteInventorySessionMutation.Field()