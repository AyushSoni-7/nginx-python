from flask import Flask
from flask_cors import CORS
from views import ROUTES
import os 


def create_app():
    flask_app = Flask(__name__)
    CORS(flask_app)
    for route in ROUTES:
        flask_app.register_blueprint(route)
    return flask_app


if __name__ == "__main__":
    PORT = os.environ.get("PORT", 5000)
    app = create_app()
    app.run(host="0.0.0.0", port=PORT)

