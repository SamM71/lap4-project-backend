from ..models.Recipe import Recipe
from werkzeug import exceptions
from flask import jsonify, request
from .. import db
from sqlalchemy import func

def index():
  try:
    recipes = Recipe.query.all()
    data = [r.json for r in recipes]
    return jsonify({"recipes": data})
  except:
    raise exceptions.NotFound("No recipes found.")
  
def show(id):
  try:
    recipe = Recipe.query.filter_by(id=id).first()
    return jsonify({"recipe": recipe.json}), 200
  except:
    raise exceptions.NotFound("Recipe not found.")
  
def show_by_name(name):
  try:
    recipe = Recipe.query.filter_by(name=name).first()
    return jsonify({"recipe": recipe.json}), 200
  except:
    raise exceptions.NotFound("Recipe not found.")


def create():
  try:
    user_id, name, culture, ingredients, steps, description, img_url = request.json.values()
    new_recipe = Recipe(user_id, name, culture, ingredients, steps, description, img_url)
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({"new_recipe": new_recipe.json}), 201
  except:
    raise exceptions.BadRequest(f"Unable to create new recipe with data provided.")
  
def update(id):
  try:
    data = request.json
    recipe = Recipe.query.filter_by(id=id).first()

    for (attr, val) in data.items():
      if hasattr(recipe, attr):
        setattr(recipe, attr, val)

    db.session.commit()
    return jsonify({"data": recipe.json})
  except:
    raise exceptions.BadRequest(f"Unable to update recipe with data provided.")
  
def delete(id):
  try:
    recipe = Recipe.query.filter_by(id=id).first()
    db.session.delete(recipe)
    db.session.commit()
    return f"Recipe deleted"
  except:
    raise exceptions.InternalServerError(f"Unable to delete recipe.")
  
def get_last():
  try:
    recipe = db.session.query(func.max(Recipe.id)).all()
    print(recipe[0][0])
    id = int(recipe[0][0])
    # return jsonify({"id": recipe[0][0]}), 200
    return show(id)
  except:
    raise exceptions.NotFound("Recipe not found.")