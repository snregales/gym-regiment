"""
GraphQL views.

Since this is going to be a graphQL application,
The only route will be /graphql
"""

from flask import Blueprint, render_template

BP = Blueprint("graphql", __name__, url_prefix="/graphql", static_folder="../static")


@BP.route("/")
def index():
    """
    When graphql route is requested funtion returns a str response.

    :return :type str: responds string
    """
    return render_template("graphql/index.html")
