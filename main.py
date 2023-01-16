# flask app using strawberry graphql
from flask import Flask
from strawberry.flask.views import GraphQLView

if __name__ == "__main__":
    app = Flask(__name__)

    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view(
            "graphql",
            schema=schema,
            graphiql=True,
        ),
    )
    app.run(host="0.0.0.0", port=5001)