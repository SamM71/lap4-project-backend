from flask import jsonify, request, Blueprint
from application import app
from ..controllers.post import index, show, create, update, delete

post_bp = Blueprint('post_bp', __name__)

@app.route("/posts", methods=["GET", "POST"])
def handle_posts():
  if request.method == "GET":
    return index()
  if request.method == "POST":
    return create()
  
@app.route("/posts/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_post(id):
  if request.method == "GET":
    return show(id)
  if request.method == "PATCH":
    return update(id)
  if request.method == "DELETE":
    return delete(id)
