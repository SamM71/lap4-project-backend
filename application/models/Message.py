from application import app, db

app.app_context().push()


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(500), nullable=False)


def __init__(self, username, text):
    self.username = username
    self.text = text


def __repr__(self):
    return f"Dialogue(id: {self.id}, username: {self.username}, text: {self.text})"


@property
def json(self):
    return {"id": self.id, "username": self.username, "text": self.text}  # remove password?