from application import app, db

app.app_context().push()


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    dialogue_id = db.Column(db.Integer, db.ForeignKey('dialogues.dialogue_id'), nullable=False)
    # dialogue = db.relationship('Dialogue', backref='dialogues', lazy=True)

    def __init__(self, username, text, dialogue_id):
        self.username = username
        self.text = text
        self.dialogue_id = dialogue_id

    def __repr__(self):
        return f"Message(id: {self.id}, username: {self.username}, text: {self.text})"

    @property
    def json(self):
        return {"id": self.id, "username": self.username, "text": self.text}

    # remove password?
