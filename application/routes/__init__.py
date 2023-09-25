from flask import jsonify, request, Blueprint
from werkzeug import exceptions
from application import app
from .user import user_bp
from .recipe import recipe_bp

app.register_blueprint(user_bp)
app.register_blueprint(recipe_bp)

@app.route("/")
def hello_world():
  return jsonify({
    "message": "Welcome"
  }), 200

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
  return jsonify({"error": f"{err}"}), 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
  return jsonify({"error": f"{err}"}), 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
  return jsonify({"error": f"{err}"})