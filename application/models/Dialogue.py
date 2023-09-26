from application import app, db

app.app_context().push()


class Dialogue(db.Model):
    __tablename__ = "dialogues"
    username = db.Column(db.String(100), nullable=False)
    receiver = db.Column(db.String(100), nullable=False)
    dialogue_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, username, receiver, dialogue_id):
        self.username = username
        self.receiver = receiver
        self.dialogue_id = dialogue_id

    def __repr__(self):
        return f"Dialogue(id: {self.id}, username: {self.username}, receiver: {self.receiver})"

    @property
    def json(self):
        return {"id": self.id, "username": self.username, "receiver": self.receiver, "title": self.title}
