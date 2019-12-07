"""Token Schema Module."""

from flask_graphql_auth import AuthInfoField
from graphene import ObjectType, String, Union


class MessageField(ObjectType):
    """MessageField."""

    message = String()


class ProtectedUnion(Union):
    """ProtectedUnion is a union between MessageField and AuthInfoField."""

    class Meta:
        """Tels the api user what to expect from this object."""

        types = (MessageField, AuthInfoField)

    @classmethod
    def resolve_type(cls, instance, info):
        """
        Resolve_type is a class method that resolves the type of the object that will be return.

        This is done since the object return is not obsolute by this schema function
        :param instance: type: Union[MessageField, AuthInfoField]: object return to the user
        :param info type:...
        :return the instance type of the object
        """
        return type(instance)
