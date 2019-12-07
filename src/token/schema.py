"""Token Schema Module."""

from typing import Union

from flask_graphql_auth import AuthInfoField
from graphene import ObjectType, String
from graphene import Union as GraphUnion
from graphql.execution.base import ResolveInfo


class MessageField(ObjectType):
    """MessageField."""

    message = String()


class ProtectedUnion(GraphUnion):
    """ProtectedUnion is a union between MessageField and AuthInfoField."""

    class Meta:
        """Tels the api user what to expect from this object."""

        types = (MessageField, AuthInfoField)

    @classmethod
    def resolve_type(
        cls, instance: Union[MessageField, AuthInfoField], info: ResolveInfo
    ) -> Union[MessageField, AuthInfoField]:
        """
        Resolve_type is a class method that resolves the type of the object that will be return.

        This is done since the object return is not obsolute by this schema function
        :param instance: type: Union[MessageField, AuthInfoField]: object return to the user
        :param info :type ResolveInfo
        :return the instance type of the object
        """
        return type(instance)
