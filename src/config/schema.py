"""Configuration Schema module, this is where all project queries will be register."""

from graphene import ObjectType, Schema
from graphene.relay import Node

from src.token.mutation import Mutations as TokenMutation
from src.token.query import Query as TokenQuery
from src.user.mutation import Mutations as UserMutation
from src.user.query import Query as UserQuery


class Query(UserQuery, TokenQuery, ObjectType):
    """All GraphQL Queries in project."""

    node = Node.Field()


class Mutation(UserMutation, TokenMutation, ObjectType):
    """All GraphQL Mutations in project."""


SCHEMA = Schema(query=Query, mutation=Mutation)
