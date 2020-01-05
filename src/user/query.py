"""User query module."""

import logging
from typing import List

from flask_graphql_auth import get_jwt_identity, query_header_jwt_required
from graphene import Field
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphql.execution.base import ResolveInfo

from src.utils.node import NodeQuery

from .models import User as UserModel
from .schema import RoleConnection, User, UserConnection

logger = logging.getLogger(__name__)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(console)


class Query(NodeQuery):
    """All querable schemas are register here."""

    me = Field(User)
    users = SQLAlchemyConnectionField(UserConnection) 
    # roles = SQLAlchemyConnectionField(RoleConnection) 

    # pylint: disable=no-self-use
    @query_header_jwt_required
    def resolve_me(self, info: ResolveInfo) -> User:
        """Resolve the User object query that is given by info.

        :param info :type ResolveInfo: desired response data
        :return :type User
        """
        return UserModel.query.filter(UserModel.username == get_jwt_identity()).first()
