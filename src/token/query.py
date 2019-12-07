"""Token Query Module."""

from flask_graphql_auth import query_header_jwt_required
from graphene import Field

from .schema import MessageField, ProtectedUnion


class Query:
    """Token Query class."""

    protected = Field(ProtectedUnion)

    @query_header_jwt_required
    def resolve_protected(self, info):
        """Resolver for protected, user authentication is required."""
        return MessageField(message="Hello World!")
