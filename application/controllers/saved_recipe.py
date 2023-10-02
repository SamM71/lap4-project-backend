from ..models.Saved_Recipe import Saved_Recipe
from ..models.Recipe import Recipe
from werkzeug import exceptions
from flask import jsonify, request
from .. import db

def index(user_id):
  try:
    # recipes = db.session.query(Saved_Recipe, Recipe).filter_by(user_id=user_id).filter(Saved_Recipe, Recipe.id==Saved_Recipe.recipe_id).all()
    recipes = db.session.query(Recipe).join(Saved_Recipe).filter_by(user_id=user_id).all()
    data = [r.json for r in recipes]
    return jsonify({"saved_recipes": data}), 200
  except:
    raise exceptions.NotFound("No saved recipes found for user.")

def create(user_id, recipe_id):
  try:
    # user_id, recipe_id = request.json.values()
    check = Saved_Recipe.query.filter_by(user_id=user_id, recipe_id=recipe_id).first()
    if check:
      raise exceptions.BadRequest(f"as recipe already saved.")
    new_recipe = Saved_Recipe(user_id, recipe_id)
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({"new_saved_recipe": new_recipe.json}), 201
  except exceptions.BadRequest as e:
    return jsonify({"error": str(e)})
  except:
    raise exceptions.InternalServerError("Unable to save recipe.")
  
def delete(user_id, recipe_id):
  try:
    recipe = Saved_Recipe.query.filter_by(user_id=user_id, recipe_id=recipe_id).first()
    db.session.delete(recipe)
    db.session.commit()
    return f"Saved recipe deleted"
  except:
    raise exceptions.InternalServerError(f"Unable to delete recipe.")