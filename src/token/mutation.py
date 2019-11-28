"""Token Mutation Module."""
from flask_graphql_auth import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    mutation_jwt_refresh_token_required,
    mutation_jwt_required,
)
from graphene import Field, Mutation, String

from .schema import MessageField, ProtectedUnion


class AuthMutation(Mutation):
    access_token = String()
    refresh_token = String()

    class Arguments(object):
        username = String()
        password = String()

    @classmethod
    def mutate(cls, _, info, username, password):
        return AuthMutation(
            access_token=create_access_token(username),
            refresh_token=create_refresh_token(username),
        )


class ProtectedMutation(Mutation):
    message = Field(ProtectedUnion)

    class Arguments(object):
        token = String()

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info):
        return ProtectedMutation(
            message=MessageField(message="Protected mutation works")
        )


class RefreshMutation(Mutation):
    new_token = String()

    class Arguments(object):
        refresh_token = String()

    @classmethod
    @mutation_jwt_refresh_token_required
    def mutate(self, _):
        current_user = get_jwt_identity()
        return RefreshMutation(new_token=create_access_token(identity=current_user))


class Mutations:
    auth = AuthMutation.Field()
    refresh = RefreshMutation.Field()
    protected = ProtectedMutation.Field()
