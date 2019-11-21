"""Query module where all project queries will be register."""

from graphene import List, ObjectType, Schema

from src.user.schema import Role, User


class Query(ObjectType):
    """All querable schemas are register here."""

    users = List(User)
    roles = List(Role)

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


SCHEMA = Schema(query=Query)
