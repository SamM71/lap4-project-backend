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
  
def show(id):
  try:
    user = User.query.filter_by(id=id).first()
    return jsonify({"user": user.json}), 200
  except:
    raise exceptions.NotFound("User not found")
