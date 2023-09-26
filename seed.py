from application import db
from application.models.User import User
from application.models.Recipe import Recipe
from application.models.Saved_Recipe import Saved_Recipe
from application.models.Dialogue import Dialogue
from application.models.Message import Message
from application.models.Token import Token



db.drop_all()
db.create_all()

entry1 = User(name="Sam", email="sam@example.com", username="sam1", password="jkl")
entry2 = User(name="Rubina", email="rubina@example.com", username="rubina1", password="jkl")
entry3 = User(name="Charlie", email="charlie@example.com", username="charlie1", password="jkl")
entry4 = User(name="Ranti", email="ranti@example.com", username="ranti1", password="jkl")
entry5 = User(name="Hasan", email="hasan@example.com", username="hasan1", password="jkl")
entry6 = Recipe(user_id=1, name="recipe1", culture="culture1", description="example recipe", img_url="url")
entry7 = Saved_Recipe(user_id=2, recipe_id=1)
entry8 = Dialogue(username="Charlie", receiver="Sam", title="charlie-sam")
entry9 = Message(username="Charlie", text="Hello, I am a message")
entry10 = Message(username="Rubina", text="Hello")
entry11 = Token(user_id=1, token='hbkdhcvhcsvcgsvchsvchlsl')
entry12 = Dialogue(username="Charlie", receiver="sam1", title="charlie-sam1")
entry13 = Dialogue(username="Charlie", receiver="rubina1", title="charlie-rubina1")
entry14 = Dialogue(username="Charlie", receiver="charlie1", title="charlie-charlie1")
entry15 = Dialogue(username="Charlie", receiver="ranti1", title="charlie-ranti1")
entry16 = Dialogue(username="Charlie", receiver="hasan1", title="charlie-hasan1")
db.session.add_all([entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, entry12,
                    entry13, entry14, entry15, entry16])
db.session.commit()


