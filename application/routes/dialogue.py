from flask import jsonify, request, Blueprint
from application import app
from ..controllers.dialogue import index, create

dialogue_bp = Blueprint('dialogue_bp', __name__)


@app.route("/dialogues")
def handle_dialogues():
    return index()
    # elif request.method == "POST":
    #     return create()


@app.route("/dialogues", methods=["POST"])
def handle_dialogue():
    if request.method == "POST":
        return create()
