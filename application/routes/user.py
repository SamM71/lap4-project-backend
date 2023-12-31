from flask import jsonify, request, Blueprint
from application import app
from ..controllers.user import index, show, create, update, delete, show_by_username, register, login, index_token, destroy_token
from ..models.User import User

user_bp = Blueprint('user_bp', __name__)


@app.route("/users", methods=["GET", "POST"])
def handle_users():
    if request.method == "GET":
        return index()
    if request.method == "POST":
        return create()

# @app.route("/users/<email>", methods=["GET"])
# def check_email_availability(email):
#     user_with_email = User.query.filter_by(email=email).first()
#     if user_with_email is not None:
#         available = False
#     else:
#         available = True
#     return jsonify({"available": available})

# @app.route("/users/<username>", methods=["GET"])
# def check_username_availability(username):
#     user_with_username = User.query.filter_by(username=username).first()
#     if user_with_username is not None:
#         available = False
#     else:
#         available = True
#     return jsonify({"available": available})

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

@app.route("/users/tokens", methods=["GET"])
def handle_tokens():
   if request.method == "GET":
      return index_token()
   
@app.route("/users/tokens/<int:id>", methods=["DELETE"])
def handle_delete_token(id):
   if request.method == "DELETE":
      return destroy_token(id)
