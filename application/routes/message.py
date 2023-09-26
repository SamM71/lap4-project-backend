from flask import jsonify, request, Blueprint
from application import app
from ..controllers.message import index, create

message_bp = Blueprint('message_bp', __name__)


@app.route("/messages", methods=["GET", "POST"])
def handle_messages():
    if request.method == "GET":
        return index()
    elif request.method == "POST":
        return create()




