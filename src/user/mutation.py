"""All Mutations from user module."""
from graphene import Mutation, String
from graphql.execution.base import ResolveInfo

from src.config.database import SurrogatePK
from src.user.models import Role, User


class CreateUser(SurrogatePK, Mutation):
    """Creation resolver class for User model."""

    # Data the server can send back to the client.
    id = String()  # id is shadowing build in python key id
    email = String()

    class Arguments:
        """Data you can send to the server."""

        password = String()
        email = String()

    # pylint: disable=no-self-use
    def mutate(
        self, info: ResolveInfo, email: str, password: str, **kwargs
    ) -> "CreateUser":
        """
        Creates a user in the database using the data sent by the user.

        :param info :type ResolveInfo
        :param email :type str: user's email
        :param password :type str: user's unhashed password
        :return :type CreateUser
        """
        user = User(email=email, password=password, **kwargs)
        user.save()

        return CreateUser(id=user.id, email=user.email)


class CreateRole(SurrogatePK, Mutation):
    """Creation resolver class for Role model."""

    # Data the server can send back to the client.
    id = String()  # id is shadowing build in python key id
    name = String()

    class Arguments:
        """Data you can send to the server."""

        name = String()

    # pylint: disable=no-self-use
    def mutate(self, info: ResolveInfo, name: str, **kwargs) -> "CreateRole":
        """
        Creates a user in the database using the data sent by the user.

        :param info :type ResolveInfo: desired response data
        :param name :type str: name of the role
        :return :type CreateRole
        """
        role = Role(name=name, **kwargs)
        role.save()

        return CreateRole(id=role.id, name=role.name)


class ChangePassword(Mutation):
    """Mutation class for changing password."""

    # Data the server can send back to the client.
    message = String()

    class Arguments:
        """Data you can send to the server."""

        current_password = String()
        new_password = String()

    # pylint: disable=no-self-use
    def mutate(
        self, info: ResolveInfo, current_password: str, new_password: str
    ) -> str:
        """Change a user's password."""


class Mutations:
    """Mutations used for user module."""

    create_user = CreateUser.Field()
    create_role = CreateRole.Field()
    change_password = ChangePassword.Field()
