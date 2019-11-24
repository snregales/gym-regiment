"""Configuration Schema module, this is where all project queries will be register."""

from graphene import Schema

from src.user.query import Query

SCHEMA = Schema(query=Query)
