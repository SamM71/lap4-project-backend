from ..models.Message import Message
from werkzeug import exceptions
from flask import jsonify, request
from .. import db
from ..models.Message import Message


def index():
    messages = Message.query.all()
    data = [m.json for m in messages]
    print(messages)
    return jsonify({"messages": data})


def create():
    username, text, dialogue_id = request.json.values()
    new_message = Message(username, text, dialogue_id)
    db.session.add(new_message)
    db.session.commit()
    messages = Message.query.all()
    data = [m.json for m in messages]
    print(messages)
    return jsonify({"messages": data})




