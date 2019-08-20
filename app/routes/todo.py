from flask import Blueprint
from app.models import Todo
from app.serealizer import TodoSchema


bp_todos = Blueprint("todos", __name__)


@bp_todos.route("/list", methods=["GET"])
def list_todos():
    result = Todo.query.all()
    return TodoSchema(many=True).jsonify(result), 200
