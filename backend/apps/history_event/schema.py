import graphene
from graphene_django import DjangoObjectType
from .models import HistoryEvent

EventTypeEnum = graphene.Enum.from_enum(HistoryEvent.EventType)


class HistoryEventType(DjangoObjectType):
    class Meta:
        model = HistoryEvent


class Query(graphene.ObjectType):
    history_events = graphene.List(HistoryEventType)

    def resolve_history_events(self, info, **kwargs):
        return HistoryEvent.objects.all()

# MUTATIONS


# CREATE
class CreateHistoryEventMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        #name = graphene.String(required=True)
        asset = graphene.ID()
        start_date = graphene.DateTime()
        end_date = graphene.DateTime()
        event_type = EventTypeEnum()
        description = graphene.String()

    # The class attributes define the response of the mutation
    history_event = graphene.Field(HistoryEventType)

    @classmethod
    def mutate(cls, root, info, asset, start_date, end_date, event_type, description):
        history_event = HistoryEvent.objects.create(
            asset_id=asset,
            start_date=start_date,
            end_date=end_date,
            event_type=event_type,
            description=description
        )

        # Notice we return an instance of this mutation
        return CreateHistoryEventMutation(history_event=history_event)


# UPDATE
class UpdateHistoryEventMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()
        asset = graphene.ID()
        start_date = graphene.DateTime()
        end_date = graphene.DateTime()
        event_type = EventTypeEnum()
        description = graphene.String()

    # The class attributes define the response of the mutation
    history_event = graphene.Field(HistoryEventType)

    @classmethod
    def mutate(cls, root, info, id, asset, start_date, end_date, event_type, description):
        history_event = HistoryEvent.objects.get(pk=id)
        history_event.asset = asset
        history_event.start_date = start_date
        history_event.end_date = end_date
        history_event.event_type = event_type
        if description is not None:
            history_event.description = description

        history_event.save()

        # Notice we return an instance of this mutation
        return UpdateHistoryEventMutation(history_event=history_event)


# DELETE
class DeleteHistoryEventMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    # The class attributes define the response of the mutation
    deleted = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        deleted = True
        try:
            history_event = HistoryEvent.objects.get(pk=id)  # asset ou id?
            history_event.delete()
        except HistoryEvent.DoesNotExist:
            deleted = False

        # Notice we return an instance of this mutation
        return DeleteHistoryEventMutation(deleted=deleted)


# MUTATIONS
class Mutation(graphene.ObjectType):
    create_history_event = CreateHistoryEventMutation.Field()
    update_history_event = UpdateHistoryEventMutation.Field()
    delete_history_event = DeleteHistoryEventMutation.Field()
