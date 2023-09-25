from ..models.User import User
from werkzeug import exceptions
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify, request
from application import db
import logging

# logging.basicConfig(filename='app.log', level=logging.ERROR)


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
  
def show_by_username(username):
  try:
    user = User.query.filter_by(username=username).first()
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
  
def register(): 
  try:
    username, email, name, password = request.json.values()

    print('input values:', username, email, name, password)
    
    if not username or not password or not email or not name: 
      raise exceptions.BadRequest(f'Unable to register, all fields need to be filled')
    elif User.query.filter_by(username = username).first():
      raise exceptions.BadRequest(f'User ${username} already exists')
    elif User.query.filter_by(email=email).first():
      raise exceptions.BadRequest(f'User with email ${email} already exists')
    else: 
      hashed_password = generate_password_hash(password, method='scrypt')
      print('hashed password:', hashed_password)
      new_user = User(username=username, email=email, name=name, password=hashed_password)
      print('new user:', new_user.id)
      print('new user:', new_user.username)
      print('new user:', new_user.email)
      print('new user:', new_user.name)
      print('new user:', new_user.password)
      print('up to here all ok')
      db.session.add(new_user)
      
      print('issue maybe starts here')
      db.session.commit()
      print('line , maybe here????')
      return jsonify({"message": "Registration successful!", "user": new_user.json}), 201
  except exceptions.BadRequest as e:
      return jsonify({"error": str(e)}), 400
  except Exception as e:
      logging.error(f"An error occurred: {str(e)}")
      return jsonify({"error": "Unable to register, please try again later."}), 500

