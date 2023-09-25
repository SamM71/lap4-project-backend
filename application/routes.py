from flask import jsonify, request
from werkzeug import exceptions
from application import app, db
from application.models import User
from .controllers import index, show

@app.route("/")
def hello_world():
  return jsonify({
    "message": "Welcome"
  }), 200

@app.route("/users", methods=["GET", "POST"])
def handle_users():
  if request.method == "GET":
    return index()
  
@app.route("/users/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_user(id):
  if request.method == "GET":
    return show(id)


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
  return jsonify({"error": f"{err}"}), 404