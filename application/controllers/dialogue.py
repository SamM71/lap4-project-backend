from ..models.Dialogue import Dialogue
from werkzeug import exceptions
from flask import jsonify, request
from .. import db


def index():
    dialogues = Dialogue.query.all()
    data = [d.json for d in dialogues]
    return jsonify({"dialogues": data})


def create():
    username, receiver, dialogue_id = request.json.values()
    print(username)
    dialogue = Dialogue.query.filter_by(dialogue_id=dialogue_id).first()
    if dialogue:
        return jsonify({"dialogue": dialogue.json}), 200
    else:
        return jsonify({"error": "No dialogue found"})


def show(id):
    dialogue = Dialogue.query.filter_by(dialogue_id=id).first()
    return jsonify({"dialogue": dialogue.json})

