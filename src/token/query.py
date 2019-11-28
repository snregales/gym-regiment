"""Token Query Module."""

from flask_graphql_auth import query_jwt_required
from graphene import Field, String

from .schema import MessageField, ProtectedUnion


class Query:
    protected = Field(type=ProtectedUnion, token=String())

    @query_jwt_required
    def resolve_protected(self, info):
        return MessageField(message="Hello World!")
