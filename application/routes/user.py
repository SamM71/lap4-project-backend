from flask import jsonify, request, Blueprint
from application import app
from ..controllers.user import index, show, create, update, delete, show_by_username

user_bp = Blueprint('user_bp', __name__)


@user_bp.route("/users", methods=["GET", "POST"])
def handle_users():
    if request.method == "GET":
        return index()
    if request.method == "POST":
        return create()


@app.route("/users/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_user(id):
    if request.method == "GET":
        return show(id)
    if request.method == "PATCH":
        return update(id)
    if request.method == "DELETE":
        return delete(id)


@app.route("/users/<username>", methods=["GET"])
def handle_user_by_username(username):
    if request.method == "GET":
        return show_by_username(username)
