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
    raise exceptions.NotFound("No users found.")
  
def show(id):
  try:
    user = User.query.filter_by(id=id).first()
    return jsonify({"user": user.json}), 200
  except:
    raise exceptions.NotFound("User not found.")

def create():
  try:
    username, email, name, password = request.json.values()
    new_user = User(username, email, name, password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"new_user": new_user.json}), 201
  except:
    raise exceptions.BadRequest(f"Unable to create new user with data provided.")
  
def update(id):
  try:
    data = request.json
    user = User.query.filter_by(id=id).first()

    for (attr, val) in data.items():
      if hasattr(user, attr):
        setattr(user, attr, val)

    db.session.commit()
    return jsonify({"data": user.json})
  except:
    raise exceptions.BadRequest(f"Unable to update user with data provided.")
  
def delete(id):
  try:
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return f"User deleted"
  except:
    raise exceptions.InternalServerError(f"Unable to delete user.")