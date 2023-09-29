from application import app, db

app.app_context().push()


class Recipe(db.Model):
    __tablename__ = "recipes"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    culture = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.JSON, nullable=False)
    steps = db.Column(db.JSON, nullable=False)
    description = db.Column(db.String(5000), nullable=False)
    img_url = db.Column(db.String(100))
    saved_recipes = db.relationship('Saved_Recipe', backref='recipes', lazy=True)
    posts = db.relationship('Post', backref='recipes', lazy=True)

    def __init__(self, user_id, name, culture, ingredients, steps, description, img_url):
        self.user_id = user_id
        self.name = name
        self.culture = culture
        self.ingredients = ingredients
        self.steps = steps
        self.description = description
        self.img_url = img_url

    def __repr__(self):
        return f"Recipe(id: {self.id}, user_id: {self.user_id}, name: {self.name})"

    @property
    def json(self):
        return {"id": self.id, "user_id": self.user_id, "name": self.name, "culture": self.culture, "ingredients": self.ingredients, "steps": self.steps, "description": self.description, "img_url": self.img_url}
