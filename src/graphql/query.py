from graphene import Schema, ObjectType, relay
from graphene_sqlalchemy import SQLAlchemyConnectionField

from src.user.schema import User, Role


class Query(ObjectType):
    """register all schema queries are register here"""
    node = relay.Node.Field()
    all_users = SQLAlchemyConnectionField(User)
    all_roles = SQLAlchemyConnectionField(Role)


SCHEMA = Schema(
    query=Query,
    types=[
        User,
        Role,])