from flask.cli import FlaskGroup
from application import app, db
from application.models.User import User
from application.models.Recipe import Recipe
from application.models.Saved_Recipe import Saved_Recipe
from application.models.Dialogue import Dialogue
from application.models.Message import Message
from application.models.Token import Token
from application.models.Post import Post
from application.models.Comment import Comment

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():

  db.drop_all()
  db.create_all()

  entry1 = User(name="Sam", email="sam@example.com", username="sam1", password="jkl")
  entry2 = User(name="Rubina", email="rubina@example.com", username="rubina1", password="jkl")
  entry3 = User(name="Charlie", email="charlie@example.com", username="charlie1", password="jkl")
  entry4 = User(name="Ranti", email="ranti@example.com", username="ranti1", password="jkl")
  entry5 = User(name="Hasan", email="hasan@example.com", username="hasan1", password="jkl")
  entry6 = Recipe(user_id=1, name="recipe1", culture="culture1", description="example recipe", img_url="url")
  entry7 = Saved_Recipe(user_id=2, recipe_id=1)
  entry9 = Message(username="charlie", text="Hello, I am a message", dialogue_id=1)
  entry10 = Message(username="rubina1", text="Hello", dialogue_id=2)
  entry11 = Token(user_id=1, token='hbkdhcvhcsvcgsvchsvchlsl')
  entry12 = Dialogue(username="charlie", receiver="sam1", dialogue_id=1)
  entry13 = Dialogue(username="charlie", receiver="rubina1", dialogue_id=2)
  entry14 = Dialogue(username="charlie", receiver="charlie1", dialogue_id=3)
  entry15 = Dialogue(username="charlie", receiver="ranti1", dialogue_id=4)
  entry16 = Dialogue(username="charlie", receiver="hasan1", dialogue_id=5)
  entry17 = Post(user_id=1, recipe_id=1, description="A very nice dish", story="I ate this with my family", img_url="url")
  entry18 = Comment(user_id=4, post_id=1, text="nice post!")

  db.session.add_all([entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry9, entry10, entry11, entry12,
                      entry13, entry14, entry15, entry16, entry17, entry18])
  db.session.commit()

if __name__ == "__main__":
  cli()