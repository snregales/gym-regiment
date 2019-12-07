"""User query module."""

import logging
from typing import List

from flask_graphql_auth import get_jwt_identity, query_header_jwt_required
from graphene import Field
from graphene import List as GraphList
from graphql.execution.base import ResolveInfo

from src.user.models import User as UserModel
from src.user.schema import Role, User

logger = logging.getLogger(__name__)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(console)


class Query:
    """All querable schemas are register here."""

    me = Field(User)
    users = GraphList(User)
    roles = GraphList(Role)

    # pylint: disable=no-self-use
    @query_header_jwt_required
    def resolve_me(self, info: ResolveInfo) -> User:
        """Resolve the User object query that is given by info.

        :param info :type ResolveInfo: desired response data
        :return :type User
        """
        return UserModel.query.filter(UserModel.email == get_jwt_identity()).first()

    # pylint: disable=no-self-use
    def resolve_users(self, info: ResolveInfo) -> List[User]:
        # self is needed, in order extract user's desired response data
        """
        Resolve the User query list that is given by info.

        :param info :type ResolveInfo: desired response data
        :return :type List[User]
        """
        return User.get_query(info).all()

    # pylint: disable=no-self-use
    def resolve_roles(self, info: ResolveInfo) -> List[Role]:
        # self is needed, in order extract user's desired response data
        """
        Resolve the Role query that is given by info.

        :param info :type ResolveInfo: desired response data
        :return :type List[Role]:
        """
        return Role.get_query(info).all()
