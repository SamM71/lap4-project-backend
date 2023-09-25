from ..models.Dialogue import Dialogue
from werkzeug import exceptions
from flask import jsonify, request
from .. import db


def index():
    dialogues = Dialogue.query.all()
    data = [d.json for d in dialogues]
    return jsonify({"dialogues": data})
