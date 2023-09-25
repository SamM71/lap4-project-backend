from flask import jsonify, request
from werkzeug import exceptions
from application import app, db

@app.route("/")
def hello_world():
  return jsonify({
    "message": "Welcome"
  }), 200