from flask import request, Blueprint
from application import app
from ..controllers.comment import index_by_pid, show, create, update, delete

comment_bp = Blueprint('comment_bp', __name__)

@app.route("/posts/<int:pid>/comments", methods=["GET", "POST"])
def handle_comments(pid):
  if request.method == "GET":
    return index_by_pid(pid)
  if request.method == "POST":
    return create(pid)
  
@app.route("/posts/<int:pid>/comments/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_comment(pid, id):
  if request.method == "GET":
    return show(id)
  if request.method == "PATCH":
    return update(id)
  if request.method == "DELETE":
    return delete(id)
