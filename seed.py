from application import db
from application.models.User import User

db.drop_all()
db.create_all()

entry1 = User(name="Sam", email="sam@example.com", username="sam1", password="jkl")
entry2 = User(name="Rubina", email="rubina@example.com", username="rubina1", password="jkl")
entry3 = User(name="Charlie", email="charlie@example.com", username="charlie1", password="jkl")
entry4 = User(name="Ranti", email="ranti@example.com", username="ranti1", password="jkl")
entry5 = User(name="Hasan", email="hasan@example.com", username="hasan1", password="jkl")

db.session.add_all([entry1, entry2, entry3, entry4, entry5])
db.session.commit()
