from application import app, db

app.app_context().push()


class Dialogue(db.Model):
    __tablename__ = "dialogues"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    receiver = db.Column(db.String(100), nullable=False)


def __init__(self, username, receiver):
    self.username = username
    self.receiver = receiver


def __repr__(self):
    return f"Dialogue(id: {self.id}, username: {self.username}, receiver: {self.receiver})"


@property
def json(self):
    return {"id": self.id, "username": self.username, "email": self.email, "name": self.name,
            "password": self.password}  # remove password?