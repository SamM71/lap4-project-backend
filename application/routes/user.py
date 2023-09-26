from flask import jsonify, request, Blueprint
from application import app
from ..controllers.user import index, show, create, update, delete, show_by_username, register, login

user_bp = Blueprint('user_bp', __name__)

@app.route("/users", methods=["GET", "POST"])
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
  
@app.route("/users/register", methods=["POST"])
def handle_register():
  if request.method == "POST":
    return register()

@app.route("/users/login", methods=["POST"])
def handle_login():
  if request.method == "POST":
    return login()
