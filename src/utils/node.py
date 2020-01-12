"""
Gym Regiment project's utility module.

functions in this module is used by multiple app
"""

from graphene.relay import Node


class NodeMeta:
    """Base Meta class to be inherited by the meta classes of the other Schemas' inner Meta Class."""

    interfaces = (Node,)
