from graphene import Schema, ObjectType, List
from graphene_sqlalchemy import SQLAlchemyConnectionField

from src.user.schema import User, Role

class Query(ObjectType):
    """register all schema queries are register here"""
    users = List(User)
    roles = List(Role)

    def resolve_users(self, info):
        return User.get_query(info).all()

    def resolve_roles(self, info):
        return Role.get_query(info).all()


SCHEMA = Schema(query=Query)