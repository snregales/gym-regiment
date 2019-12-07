"""Token Mutation Module."""
import logging

from flask_graphql_auth import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    mutation_header_jwt_refresh_token_required,
    mutation_header_jwt_required,
)
from graphene import Field, Mutation, String
from graphql.execution.base import ResolveInfo

from .schema import MessageField, ProtectedUnion

logger = logging.getLogger(__name__)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(console)


class AuthMutation(Mutation):
    """Authentication Mutation class."""

    access_token = String()
    refresh_token = String()

    class Arguments:
        """Data you can send to the server."""

        email = String()
        password = String()

    @classmethod
    def mutate(
        cls, _, info: ResolveInfo, email: str, password: str
    ) -> "AuthMutation":
        """
        Mutate is a class method that creates an access and refresh tokens for the given user.

        :param _ :type...
        :param info :type ResolveType
        :param email :type str: User object's email
        :param password :type str: User object's password
        :return :type AuthMutation (self)
        """
        return AuthMutation(
            access_token=create_access_token(email),
            refresh_token=create_refresh_token(email),
        )


class ProtectedMutation(Mutation):
    """
    ProtectedUnion object mutation class.

    inherits from graphen.Mutate
    """

    message = Field(ProtectedUnion)

    class Arguments:
        """Data you can send to the server."""

        token = String()

    @classmethod
    @mutation_header_jwt_required
    def mutate(cls, _, info: ResolveInfo) -> "ProtectedMutation":
        """
        Mutation class method, authentication is required to access method.

        :param _ :type...
        :param info :type ResolveType
        :return :type ProtectedMutation (self)
        """
        return ProtectedMutation(
            message=MessageField(message="Protected mutation works")
        )


class RefreshMutation(Mutation):
    """
    RefreshMutation class.

    inherits from graphen.Mutate
    """

    new_token = String()

    class Arguments:
        """Data you can send to the server."""

        refresh_token = String()

    @classmethod
    @mutation_header_jwt_refresh_token_required
    def mutate(cls, _):
        """
        Mutation class method, authentication is required to access method.

        :param _ :type...
        :return :type RefreshMutation (self)
        """
        current_user = get_jwt_identity()
        return RefreshMutation(new_token=create_access_token(identity=current_user))


class Mutations:
    """
    Token's Mutations class.

    Register all mutaion from the token module
    """

    auth = AuthMutation.Field()
    refresh = RefreshMutation.Field()
    protected = ProtectedMutation.Field()
