from application import app, db
import datetime

app.app_context().push()


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    story = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String(100))
    time_posted = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, user_id, recipe_id, description, story, img_url):
        self.user_id = user_id
        self.recipe_id = recipe_id
        self.description = description
        self.story = story
        self.img_url = img_url

    def __repr__(self):
        return f"Post(id: {self.id}, user_id: {self.user_id}, recipe_id: {self.recipe_id})"

    @property
    def json(self):
        return {"id": self.id, "user_id": self.user_id, "recipe_id": self.recipe_id,
                "description": self.description, "story": self.story, "img_url": self.img_url, "time_posted": self.time_posted}
