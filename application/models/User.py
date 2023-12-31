from application import app, db

app.app_context().push()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    recipes = db.relationship('Recipe', backref='users', lazy=True)
    saved_recipes = db.relationship('Saved_Recipe', backref='users', lazy=True)
    posts = db.relationship('Post', backref='users', lazy=True)
    comments = db.relationship('Comment', backref='users', lazy=True)

    def __init__(self, username, email, name, password):
        self.username = username
        self.email = email
        self.name = name
        self.password = password

    def __repr__(self):
        return f"User(id: {self.id}, username: {self.username})"

    @property
    def json(self):
        return {"id": self.id, "username": self.username, "email": self.email, "name": self.name,
                "password": self.password}  # remove password?

