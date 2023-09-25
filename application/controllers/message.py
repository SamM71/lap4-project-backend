from ..models.Message import Message
from werkzeug import exceptions
from flask import jsonify, request
from .. import db


def index():
    try:
        messages = Message.query.all()
        data = [m.json for m in messages]
        print(data)
        return jsonify({"messages": data})
    except:
        raise exceptions.NotFound("No messages found.")


