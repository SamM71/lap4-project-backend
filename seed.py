from application import db
from application.models.User import User
<<<<<<< HEAD
=======
from application.models.Recipe import Recipe
from application.models.Saved_Recipe import Saved_Recipe
>>>>>>> 08bbe3fcc9b5de2f47a363d637bfc69d5cc969a5

db.drop_all()
db.create_all()

entry1 = User(name="Sam", email="sam@example.com", username="sam1", password="jkl")
entry2 = User(name="Rubina", email="rubina@example.com", username="rubina1", password="jkl")
entry3 = User(name="Charlie", email="charlie@example.com", username="charlie1", password="jkl")
entry4 = User(name="Ranti", email="ranti@example.com", username="ranti1", password="jkl")
entry5 = User(name="Hasan", email="hasan@example.com", username="hasan1", password="jkl")

<<<<<<< HEAD
db.session.add_all([entry1, entry2, entry3, entry4, entry5])
db.session.commit()

=======
entry6 = Recipe(user_id=1, name="recipe1", culture="culture1", description="example recipe", img_url="url")
entry7 = Saved_Recipe(user_id=2, recipe_id=1)

db.session.add_all([entry1, entry2, entry3, entry4, entry5, entry6])
db.session.commit()
>>>>>>> 08bbe3fcc9b5de2f47a363d637bfc69d5cc969a5
