"""Token Query Module."""

from flask_graphql_auth import query_header_jwt_required
from graphene import Field
from graphql.execution.base import ResolveInfo

from .schema import MessageField, ProtectedUnion


class Query:
    """Token Query class."""

    protected = Field(ProtectedUnion)

    # pylint: disable=no-self-use
    @query_header_jwt_required
    def resolve_protected(self, info: ResolveInfo) -> MessageField:
        # self is needed, in order extract user's desired response data
        """
        Resolver for protected, user authentication is required.

        :param info :type ResolveInfo
        :return :type MessageField
        """
        return MessageField(message="Hello World!")
