from flask import jsonify, request, Blueprint
from application import app
from ..controllers.dialogue import index

dialogue_bp = Blueprint('dialogue_bp', __name__)


@app.route("/dialogues")
def handle_dialogues():
    return index()
