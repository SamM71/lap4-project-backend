from flask import jsonify, request, Blueprint
from application import app
from ..controllers.message import index

recipe_bp = Blueprint('message_bp', __name__)


@app.route("/messages", methods=["GET"])
def handle_messages():
    if request.method == "GET":
        return index()

