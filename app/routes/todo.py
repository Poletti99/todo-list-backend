from flask import Blueprint, current_app, jsonify, request
from app.models import Todo
from app.serealizer import TodoSchema


bp_todos = Blueprint("todos", __name__)


@bp_todos.route("/list", methods=["GET"])
def list_todos():
    result = Todo.query.all()
    return TodoSchema(many=True).jsonify(result), 200


@bp_todos.route("/register", methods=["POST"])
def register_todo():
    todo_schema = TodoSchema()

    todo = todo_schema.load(request.json)

    current_app.db.session.add(todo)
    current_app.db.session.commit()

    return todo_schema.jsonify(todo), 201
