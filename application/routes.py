from flask import jsonify, request
from werkzeug import exceptions
from application import app, db
from application.models import User
from .controllers import index, show, create, update, delete

@app.route("/")
def hello_world():
  return jsonify({
    "message": "Welcome"
  }), 200

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


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
  return jsonify({"error": f"{err}"}), 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
  return jsonify({"error": f"{err}"}), 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
  return jsonify({"error": f"{err}"})