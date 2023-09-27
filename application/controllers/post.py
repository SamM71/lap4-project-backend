from ..models.Post import Post
from werkzeug import exceptions
from flask import jsonify, request
from .. import db

def index():
  try:
    posts = Post.query.all()
    data = [p.json for p in posts]
    return jsonify({"posts": data})
  except:
    raise exceptions.NotFound("No posts found.")
  
def show(id):
  try:
    post = Post.query.filter_by(id=id).first()
    return jsonify({"post": post.json}), 200
  except:
    raise exceptions.NotFound("Post not found.")
  
# def show_all_by_uid(user_id):
#   try:
#     posts = Post.query.filter_by(user_id=user_id)
#     data = [p.json for p in posts]
#     return jsonify({"posts": data}), 200
#   except:
#     raise exceptions.NotFound("Posts not found.")

def create():
  try:
    user_id, recipe_id, description, story, img_url = request.json.values()
    new_post = Post(user_id, recipe_id, story, description, img_url)
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"new_post": new_post.json}), 201
  except:
    raise exceptions.BadRequest(f"Unable to create new post with data provided.")
  
def update(id):
  try:
    data = request.json
    post = Post.query.filter_by(id=id).first()

    for (attr, val) in data.items():
      if hasattr(post, attr):
        setattr(post, attr, val)

    db.session.commit()
    return jsonify({"data": post.json})
  except:
    raise exceptions.BadRequest(f"Unable to update post with data provided.")
  
def delete(id):
  try:
    post = Post.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()
    return f"Post deleted"
  except:
    raise exceptions.InternalServerError(f"Unable to delete post.")