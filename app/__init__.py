import os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    cors = CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/todos.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["CORS_HEADERS"] = "Content-Type"

    return app
