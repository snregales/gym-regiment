"""User Schema Module."""

from graphene.relay import Node
from graphene_sqlalchemy import SQLAlchemyObjectType

from src.user.models import Role as RoleModel
from src.user.models import User as UserModel


class BaseMeta:
    """Base Meta class to be inherited by the meta classes of the other Schemas' inner Meta Class."""

    interfaces = (Node,)


class User(SQLAlchemyObjectType):
    """User Schema, inherits from SQLAlchemyObjectType."""

    class Meta(BaseMeta):
        """Schema Meta Class, inherits from BaseMeta."""

        model = UserModel


class Role(SQLAlchemyObjectType):
    """Role Schema, inherits from SQLAlchemyObjectType."""

    class Meta(BaseMeta):
        """Schema Meta Class, inherits from BaseMeta."""

        model = RoleModel
