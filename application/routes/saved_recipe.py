from flask import jsonify, request, Blueprint
from application import app
from ..controllers.saved_recipe import index, create, delete

saved_bp = Blueprint('saved_bp', __name__)

@app.route("/saved/<int:uid>", methods=["GET"])
def handle_srecipes(uid):
  if request.method == "GET":
    return index(uid)
  
@app.route("/saved/<int:uid>/<int:rid>", methods=["POST", "DELETE"])
def handle_srecipe(uid, rid):
  if request.method == "POST":
    return create(uid, rid)
  if request.method == "DELETE":
    return delete(uid, rid)
