import os
from flask import Flask
from flask_migrate import Migrate
from app.models import configure as config_db
from .serealizer import configure as config_ma
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    cors = CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/todos.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["CORS_HEADERS"] = "Content-Type"

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from app.routes.todo import bp_todos
    app.register_blueprint(bp_todos)

    return app
