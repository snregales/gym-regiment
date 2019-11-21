"""Project's API only view."""

from flask_graphql import GraphQLView

from src.graphql.query import SCHEMA

VIEW = GraphQLView.as_view("graphql", schema=SCHEMA, graphiql=True)
