from flask import jsonify, request, Blueprint
from application import app
from ..controllers.dialogue import index, create, show, show_user

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


@app.route("/dialogues/<int:id>", methods=["GET"])
def handle_view(id):
    if request.method == "GET":
        return show(id)


@app.route("/dialogues/<string:username>", methods=["GET"])
def handle_user_get(username):
    if request.method == "GET":
        print(f'this is the {username}')
        return show_user(username)

