"""User Schema Module."""

from graphene.relay import Connection
from graphene_sqlalchemy import SQLAlchemyObjectType

from src.user.models import Role as RoleModel
from src.user.models import User as UserModel
from src.utils.node import NodeMeta


class User(SQLAlchemyObjectType):
    """User Schema, inherits from SQLAlchemyObjectType."""

    class Meta(NodeMeta):
        """Schema Meta Class, inherits from BaseMeta."""

        model = UserModel


class UserConnection(Connection):
    """User connection schema, inherits from relay.Connection."""

    class Meta:
        """User Schema Meta class."""

        node = User


class Role(SQLAlchemyObjectType):
    """Role Schema, inherits from SQLAlchemyObjectType."""

    class Meta(NodeMeta):
        """Schema Meta Class, inherits from BaseMeta."""

        model = RoleModel


class RoleConnection(Connection):
    """Role Connection Schema, inherits from relay.Connection."""

    class Meta:
        """Role Schema Meta class."""

        node = Role
