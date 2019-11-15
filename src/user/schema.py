import graphene

from graphene.relay import Node
from graphene_sqlalchemy import SQLAlchemyObjectType

from src.user.models import User as UserModel, Role as RoleModel

class BaseMeta:
    interfaces = (Node,)


class User(SQLAlchemyObjectType):
    class Meta(BaseMeta):
        model = UserModel    


class Role(SQLAlchemyObjectType):
    class Meta(BaseMeta):
        model = RoleModel
