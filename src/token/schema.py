"""Token Schema Module"""

from flask_graphql_auth import AuthInfoField
from graphene import ObjectType, String, Union


class MessageField(ObjectType):
    message = String()


class ProtectedUnion(Union):
    class Meta:
        types = (MessageField, AuthInfoField)

    @classmethod
    def resolve_type(cls, instance, info):
        return type(instance)
