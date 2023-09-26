from ..models.User import User
from werkzeug import exceptions
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify, request
from application import db
from flask_jwt_extended import create_access_token
import logging


def index():
    print('working')
    # try:
    users = User.query.all()
    print(users)
    data = [u.json for u in users]
    return jsonify({"users": data})
    # except:
    #     raise exceptions.NotFound("No users found.")


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
    print('hello')
    print('input values:', username, email, name, password)
    
    # if not username or not email or not password or not name: 
    #   raise exceptions.BadRequest(f'Unable to register, all fields need to be filled')
    
    if User.query.filter_by(username = username).first():
      raise exceptions.BadRequest(f'User {username} already exists')
    
    elif User.query.filter_by(email=email).first():
      raise exceptions.BadRequest(f'User with email {email} already exists')
    
    else: 
      hashed_password = generate_password_hash(password, method='scrypt')
      print('hashed password:', hashed_password)
      new_user = User(username=username, email=email, name=name, password=hashed_password)
      print('new user:', new_user.id, new_user.username, new_user.email, new_user.name, new_user.password)
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
      return jsonify({"error": "Unable to register, all fields need to be filled"}), 500
  

def login():
  try: 
    username, password = request.json.values()

    print('input values:', username, password)

    if not username or not password:
      print('no username or password provided')
      raise exceptions.BadRequest('Unable to login, please input both email and password')
    
    user = User.query.filter_by(username=username).first()

    if not user:
      raise exceptions.BadRequest(f'Wrong credentials - username {username} not found')
    
    if not check_password_hash(user.password, password):
      raise exceptions.BadRequest(f'Wrong credentials - incorrect password')
    else: 
      access_token = create_access_token(identity=user.id)
      print('line 124:', access_token)
      return jsonify({"message": "logged in successfully"}), 200
    
  except exceptions.BadRequest as e:
      return jsonify({"error": str(e)}), 400  
  except:
      raise exceptions.InternalServerError('Unable to login, please try again later')
  


