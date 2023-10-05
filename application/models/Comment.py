from application import app, db
import datetime

app.app_context().push()

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    text = db.Column(db.String(100), nullable=False)
    time_posted = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, user_id, username, post_id, text):
        self.user_id = user_id
        self.username = username
        self.post_id = post_id
        self.text = text

    def __repr__(self):
        return f"Comment(id: {self.id}, user_id: {self.user_id}, post_id: {self.post_id})"

    @property
    def json(self):
        return {"id": self.id, "user_id": self.user_id, "username": self.username, "post_id": self.post_id,
                "text": self.text, "time_posted": self.time_posted}
