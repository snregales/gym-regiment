"""All Mutations from user module."""
from graphene import Mutation, String

from src.config.database import SurrogatePK
from src.user.models import Role, User


class CreateUser(SurrogatePK, Mutation):
    """Creation resolver class for User model."""

    # Data the server can send back to the client.
    id = String()  # id is shadowing build in python key id
    username = String()
    email = String()
    first_name = String()
    last_name = String()

    class Arguments:
        """Data you can send to the server."""

        password = String()
        username = String()
        email = String()
        first_name = String()
        last_name = String()

    def mutate(
        self, info, username: str, email: str, password: str, **kwargs
    ) -> "CreateUser":
        """
        Creates a user in the database using the data sent by the user.

        :param info :type ...
        :param username :type str: user's username
        :param email :type str: user's email
        :param password :type str: user's unhashed password
        :return :type CreateUser
        """
        user = User(username=username, email=email, password=password, **kwargs)
        user.save()

        return CreateUser(
            id=user.id,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
        )


class CreateRole(SurrogatePK, Mutation):
    """Creation resolver class for Role model."""

    # Data the server can send back to the client.
    id = String()  # id is shadowing build in python key id
    name = String()

    class Arguments:
        """Data you can send to the server."""

        name = String()

    def mutate(self, info, name: str, **kwargs) -> "CreateRole":
        """
        Creates a user in the database using the data sent by the user.

        :param info :type ...
        :param name :type str: name of the role
        :return :type CreateRole
        """
        role = Role(name=name, **kwargs)
        role.save()

        return CreateRole(id=role.id, name=role.name)


class Mutations:
    """Mutations used for user module."""

    create_user = CreateUser.Field()
    create_role = CreateRole.Field()
