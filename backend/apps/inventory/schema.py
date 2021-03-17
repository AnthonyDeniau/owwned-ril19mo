import graphene
from graphene_django import DjangoObjectType
from .models import InventoryItem, InventorySession

class InventorySessionType(DjangoObjectType):
    class Meta:
        model = InventorySession


class InventoryItemType(DjangoObjectType):
    class Meta:
        model = InventoryItem

# QUERY
class Query(graphene.ObjectType):
    inventory_sessions = graphene.List(InventorySessionType)
    inventory_items = graphene.List(InventoryItemType)

    def resolve_inventory_sessions(self, info, **kwargs):
        return InventorySession.objects.all()

    def resolve_inventory_items(self, info, **kwargs):
        return InventoryItem.objects.all()


# MUTATIONS

# InventorySession
class CreateInventorySessionMutation(graphene.Mutation):
    class Arguments:
        start_date = graphene.DateTime()
        end_date = graphene.DateTime()
        manager_id = graphene.ID(name="manager")
    inventory_session = graphene.Field(InventorySessionType)

    @classmethod
    def mutate(cls, root, info, start_date, end_date, manager_id):
        inventory_session = InventorySession.objects.create(start_date=start_date, end_date=end_date,
                                                            manager_id=manager_id)
        # Notice we return an instance of this mutation
        return CreateInventorySessionMutation(inventory_session=inventory_session)


class UpdateInventorySessionMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        start_date = graphene.DateTime(required=False)
        end_date = graphene.DateTime(required=False)
        manager = graphene.ID(required=False)

    inventory_session = graphene.Field(InventorySessionType)

    @classmethod
    def mutate(cls, root, info, id, start_date=None, end_date=None, manager_id=None):
        inventory_session = InventorySession.objects.get(pk=id)
        if start_date is not None:
            inventory_session.start_date = start_date
        if end_date is not None:
            inventory_session.end_date = end_date
        if manager_id is not None:
            inventory_session.manager_id = manager_id

        inventory_session.save()
        return UpdateInventorySessionMutation(inventory_session=inventory_session)


class DeleteInventorySessionMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    inventory_session = graphene.Field(InventorySessionType)

    @classmethod
    def mutate(cls, root, info, id):
        deleted = True
        try:
            inventory_session = InventorySession.objects.get(pk=id)
            inventory_session.delete()
        except InventorySession.DoesNotExist:
            deleted = False

        return DeleteInventorySessionMutation(deleted=deleted)


class Mutation(graphene.ObjectType):
    create_inventory_session = CreateInventorySessionMutation.Field()
    update_inventory_session = UpdateInventorySessionMutation.Field()
    delete_inventory_session = DeleteInventorySessionMutation.Field()
