from .models import User
from werkzeug import exceptions
from flask import jsonify, request
from . import db

def index():
  try:
    users = User.query.all()
    data = [u.json for u in users]
    return jsonify({"users": data})
  except:
    raise exceptions.NotFound("No users found")
