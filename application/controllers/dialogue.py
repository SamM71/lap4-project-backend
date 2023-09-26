from ..models.Dialogue import Dialogue
from werkzeug import exceptions
from flask import jsonify, request
from .. import db


def index():
    dialogues = Dialogue.query.all()
    data = [d.json for d in dialogues]
    return jsonify({"dialogues": data})


def create():
    username, receiver, title = request.json.values()
    print(username)
    dialogue = Dialogue.query.filter_by(title=title).first()
    if dialogue:
        return jsonify({"dialogue": dialogue.json}), 200
    else:
        return jsonify({"error": "No dialogue found"})

