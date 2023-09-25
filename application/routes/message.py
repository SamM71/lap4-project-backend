from flask import jsonify, request, Blueprint
from application import app
from ..controllers.message import index

message_bp = Blueprint('message_bp', __name__)


@app.route("/messages")
def handle_messages():
    return index()




