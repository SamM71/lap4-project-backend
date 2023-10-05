from ..models.Comment import Comment
from werkzeug import exceptions
from flask import jsonify, request
from .. import db

def index_by_pid(post_id):
  try:
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.time_posted.asc())
    data = [c.json for c in comments]
    return jsonify({"comments": data})
  except:
    raise exceptions.NotFound("No comments found.")
  
def show(id):
  try:
    comment = Comment.query.filter_by(id=id).first()
    return jsonify({"comment": comment.json}), 200
  except:
    raise exceptions.NotFound("comment not found.")

def create(post_id):
  try:
    user_id, username, text = request.json.values()
    new_comment = Comment(user_id, username, post_id, text)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"new_comment": new_comment.json}), 201
  except:
    raise exceptions.BadRequest(f"Unable to create new comment with data provided.")
  
def update(id):
  try:
    data = request.json
    comment = Comment.query.filter_by(id=id).first()

    for (attr, val) in data.items():
      if hasattr(comment, attr):
        setattr(comment, attr, val)

    db.session.commit()
    return jsonify({"data": comment.json})
  except:
    raise exceptions.BadRequest(f"Unable to update comment with data provided.")
  
def delete(id):
  try:
    comment = Comment.query.filter_by(id=id).first()
    db.session.delete(comment)
    db.session.commit()
    return f"Comment deleted"
  except:
    raise exceptions.InternalServerError(f"Unable to delete comment.")