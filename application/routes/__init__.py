from flask import jsonify, request, Blueprint
from werkzeug import exceptions
from application import app
from .user import user_bp
from .recipe import recipe_bp
from .saved_recipe import saved_bp
from .message import message_bp
from .dialogue import dialogue_bp
from .post import post_bp
from .comment import comment_bp

app.register_blueprint(user_bp)
app.register_blueprint(recipe_bp)
app.register_blueprint(saved_bp)
app.register_blueprint(message_bp)
app.register_blueprint(dialogue_bp)
app.register_blueprint(post_bp)
app.register_blueprint(comment_bp)

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