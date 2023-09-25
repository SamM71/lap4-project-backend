from ..models.Message import Message
from werkzeug import exceptions
from flask import jsonify, request
from .. import db


def index():
    messages = Message.query.all()
    data = [m.json for m in messages]
    print(messages)
    return jsonify({"messages": data})





