"""
GraphQL views.

Since this is going to be a graphQL application,
The only route will be /graphql
"""

from flask_graphql import GraphQLView

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


# from flask import Blueprint, render_template, current_app

# BP = Blueprint("graphql", __name__, url_prefix="/graphql", static_folder="../static")


# @BP.route("/")
# def index():
#     """
#     When graphql route is requested funtion returns a str response.

#     :return :type str: responds string
#     """

#     current_app.logger.info("Gym Regiment's graphql page")
#     return render_template("graphql/index.html")
