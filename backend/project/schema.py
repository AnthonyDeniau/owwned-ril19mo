import graphene

from apps.organization import schema as organization_schema
from apps.location import schema as location_schema
from apps.supplier import schema as supplier_schema
from apps.team import schema as team_schema
from apps.asset import schema as asset_schema
from apps.history_event import schema as history_event_schema
from apps.inventory import schema as inventory_schema
from apps.inventory import schema_inventory_session as inventory_session_schema
from apps.inventory import schema_inventory_item as inventory_item_schema

class Query(inventory_item_schema.Query, inventory_session_schema.Query, inventory_schema.Query, history_event_schema.Query, asset_schema.Query, team_schema.Query, supplier_schema.Query, location_schema.Query, organization_schema.Query, graphene.ObjectType):
    pass


class Mutation(inventory_item_schema.Mutation, inventory_session_schema.Mutation, team_schema.Mutation, asset_schema.Mutation, organization_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
