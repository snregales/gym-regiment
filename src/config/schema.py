"""Configuration Schema module, this is where all project queries will be register."""

from graphene import ObjectType, Schema

from src.user.mutation import Mutation as UserMutation
from src.user.query import Query as UserQuery


class Query(UserQuery, ObjectType):
    """All GraphQL Queries in project."""

    pass


class Mutation(UserMutation, ObjectType):
    """All GraphQL Mutations in project."""

    pass


SCHEMA = Schema(query=Query, mutation=Mutation)
