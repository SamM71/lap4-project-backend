from flask import jsonify, request, Blueprint
from application import app
from ..controllers.recipe import index, show, create, update, delete, show_by_name

recipe_bp = Blueprint('recipe_bp', __name__)

@app.route("/recipes", methods=["GET", "POST"])
def handle_recipes():
  if request.method == "GET":
    return index()
  if request.method == "POST":
    return create()
  
@app.route("/recipes/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_recipe(id):
  if request.method == "GET":
    return show(id)
  if request.method == "PATCH":
    return update(id)
  if request.method == "DELETE":
    return delete(id)
  
@app.route("/recipes/<name>", methods=["GET"])
def handle_recipe_by_name(name):
  if request.method == "GET":
    return show_by_name(name)
