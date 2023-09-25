from application import app, db

app.app_context().push()

class Saved_Recipe(db.Model):
  __tablename__ = "saved_recipes"
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)

  def __init__(self, user_id, recipe_id):
    self.user_id = user_id
    self.recipe_id = recipe_id

  def __repr__(self):
    return f"Saved_Recipe(id: {self.id}, user_id: {self.user_id}, recipe_id: {self.recipe_id})"
  
  @property
  def json(self):
    return {"id": self.id, "user_id": self.user_id, "recipe_id": self.recipe_id}