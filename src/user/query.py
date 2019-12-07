"""User query module."""

from flask_graphql_auth import query_header_jwt_required
from graphene import Field, List, String

from src.user.schema import Role, User


class Query:
    """All querable schemas are register here."""

    me = Field(User, username=String())
    users = List(User)
    roles = List(Role)

    @query_header_jwt_required
    def resolve_me(self, info, username):
        """
        Resolve the me query that is given by info.

        :param info :type :rules to query by
        :return :type :all users that satisfies info
        """
        import logging

        logger = logging.getLogger(__name__)
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        logger.addHandler(console)
        logger.info(info.context.headers)
        # logger.info(info.field_asts)
        # logger.info(info.schema)
        # logger.info(info.operation)
        # logger.info(info.path)
        # logger.info(user)
        # if user.is_anonymous:
        #     raise Exception("Not logged in")
        # return user

    def resolve_users(self, info):
        """
        Resolve the User query that is given by info.

        :param info :type :rules to query by
        :return :type :all users that satisfies info
        """
        return User.get_query(info).all()

    def resolve_roles(self, info):
        """
        Resolve the Role query that is given by info.

        :param info :type :rules to query by
        :return :type :all users that satisfies info
        """
        return Role.get_query(info).all()
