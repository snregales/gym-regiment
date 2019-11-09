"""Test for graphql views."""

from src.graphql.views import BP


def test_blueprint() -> None:
    """
    Test graphql's blueprint.

    :return :type None
    """
    assert BP.has_static_folder
