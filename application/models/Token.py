from application import app, db

app.app_context().push()

class Token(db.Model):
    __tablename__ = "tokens"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.relationship('User', backref='users', lazy=True)
    token = db.Column(db.String(100), nullable=False)

    def __init__ (self, user_id, token):
        self.user_id = user_id
        self.token = token


    def __repr__(self):
        return f"Token(id: {self.id}, user_id: {self.user_id}, token: {self.token})"
    
    @property
    def json(self):
        return {"id": self.id, "user_id": self.user_id, "token": self.token}
