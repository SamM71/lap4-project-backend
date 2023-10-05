from application import db
from application.models.User import User
from application.models.Recipe import Recipe
from application.models.Saved_Recipe import Saved_Recipe
from application.models.Dialogue import Dialogue
from application.models.Message import Message
from application.models.Token import Token
from application.models.Post import Post
from application.models.Comment import Comment

def add_users():
  entry1 = User(name="Sam", email="sam@example.com", username="sam1", password="jkl")
  entry2 = User(name="Rubina", email="rubina@example.com", username="rubina1", password="jkl")
  entry3 = User(name="Charlie", email="charlie@example.com", username="charlie1", password="jkl")
  entry4 = User(name="Ranti", email="ranti@example.com", username="ranti1", password="jkl")
  entry5 = User(name="Hasan", email="hasan@example.com", username="hasan1", password="jkl")
  entry6 = User(name="Gordon", email="gordon@example.com", username="chef1", password="jkl")
  db.session.add_all([entry1, entry2, entry3, entry4, entry5, entry6])
  # db.session.commit()

def add_recipes():
  entry1 = Recipe(user_id=6, name="Penne all'arrabbiata", culture="Italian", ingredients=[{'ingredient': 'penne pasta', 'amount': '340g'}, {'ingredient': 'olive oil', 'amount': '2 tbsp'}, {'ingredient': 'garlic', 'amount': '4 cloves'}, {'ingredient': 'red pepper flakes', 'amount': '1 tsp'}, {'ingredient': 'crushed tomatoes', 'amount': '400g'}, {'ingredient': 'sugar', 'amount': '1 tsp'}, {'ingredient': 'salt and pepper', 'amount': '(To taste)'}, {'ingredient': 'fresh basil leaves or parsley', 'amount': '(Optional) for garnish - '}, {'ingredient': 'greated parmesan cheese', 'amount': '(Optional) for serving - '}], steps=[{'step': 'Bring a large pot of salted water to a boil. Add the penne pasta and cook according to the package instructions until al dente. Drain the pasta and set it aside.'}, {'step': 'While the pasta is cooking, heat the olive oil in a large skillet over medium heat.'}, {'step': 'Add the minced garlic and red pepper flakes to the skillet. Sauté for about 1-2 minutes, or until the garlic becomes fragrant and slightly golden. Be careful not to burn the garlic.'}, {'step': 'Pour in the crushed tomatoes and stir to combine. Add the sugar, salt, and black pepper. Lower the heat and let the sauce simmer for about 15-20 minutes, allowing it to thicken and develop flavor. If you prefer a smoother sauce, you can use an immersion blender to puree it.'}, {'step': 'Taste the sauce and adjust the seasoning if needed. If you want it spicier, you can add more red pepper flakes.'}, {'step': 'Once the sauce is ready, add the cooked penne pasta to the skillet. Toss the pasta in the sauce, ensuring it\'s well coated. Let it cook for another 2-3 minutes to heat the pasta through.'}, {'step': 'Serve the penne all\'arrabbiata hot, garnished with fresh basil leaves or parsley if desired. You can also sprinkle grated Parmesan cheese on top for added flavor.'}], description="Penne all'arrabbiata is a classic Italian pasta dish known for its spicy tomato sauce. It's a relatively simple recipe that's bursting with flavor.", img_url="cucina/arrabbiata_oqdsuv")
  entry2 = Recipe(user_id=6, name="Chicken Pad Thai", culture="Thai", ingredients=[{'ingredient': 'tamarind paste', 'amount': '3 tbsp'}, {'ingredient': 'fish sauce', 'amount': '2 tbsp'}, {'ingredient': 'soy sauce', 'amount': '2 tbsp'}, {'ingredient': 'brown sugar', 'amount': '2 tbsp'}, {'ingredient': 'chili sauce or Sriracha', 'amount': '1 tsp'}, {'ingredient': 'rice noodles', 'amount': '225g'}, {'ingredient': 'vegetable oil', 'amount': '2 tbsp'}, {'ingredient': 'garlic, minced', 'amount': '2 cloves'}, {'ingredient': 'small onion, thinly sliced', 'amount': '1'}, {'ingredient': 'boneless, skinless chicken breast, thinly sliced into bite-sized pieces', 'amount': '1'}, {'ingredient': 'eggs, lightly beaten', 'amount': '2'}, {'ingredient': 'bean sprouts', 'amount': '1 cup'}, {'ingredient': 'green onions, chopped', 'amount': '4'}, {'ingredient': 'crushed peanuts', 'amount': '1/4 cup'}, {'ingredient': 'Lime wedges and fresh cilantro', 'amount': '(Optional) for garnish -'}], steps=[{'step': 'Soak the rice noodles in warm water for about 30 minutes or until they are pliable but still slightly firm. Drain and set aside.'}, {'step': 'In a small bowl, mix together the tamarind paste, fish sauce, soy sauce, brown sugar, and chili sauce. Adjust the flavors to your liking by adding more sugar, fish sauce, or chili sauce if needed. Set the sauce aside.'}, {'step': 'Heat the vegetable oil in a large wok or skillet over medium-high heat. Add the minced garlic and sliced onions. Stir-fry for 1-2 minutes until fragrant and the onions start to soften.'}, {'step': 'Add the sliced chicken to the wok and stir-fry until it\'s no longer pink and cooked through, about 4-5 minutes.'}, {'step': 'Push the chicken and vegetables to one side of the wok, making space for the eggs.'}, {'step': 'Pour the lightly beaten eggs into the empty side of the wok. Scramble them until they are mostly cooked.'}, {'step': 'Add the drained rice noodles to the wok along with the Pad Thai sauce you prepared earlier. Toss everything together, ensuring that the noodles are well coated with the sauce.'}, {'step': 'Stir in the bean sprouts and chopped green onions. Cook for an additional 1-2 minutes until the bean sprouts are slightly softened.'}, {'step': 'Transfer the Chicken Pad Thai to serving plates. Garnish with crushed peanuts and fresh cilantro (if desired). Serve with lime wedges on the side.'}], description="Chicken Pad Thai is a delicious and popular Thai stir-fried noodle dish.", img_url='cucina/pad_thai_moysxl')
  db.session.add_all([entry1, entry2])
  # db.session.commit()

def add_saved_recipes():
  entry1 = Saved_Recipe(user_id=2, recipe_id=1)
  db.session.add_all([entry1])
  # db.session.commit()

def add_messages():
  entry1 = Message(username="charlie", text="Hello, I am a message", dialogue_id=1)
  entry2 = Message(username="rubina1", text="Hello", dialogue_id=2)
  db.session.add_all([entry1, entry2])
  # db.session.commit()

def add_tokens():
  entry1 = Token(user_id=1, token='hbkdhcvhcsvcgsvchsvchlsl')
  db.session.add_all([entry1])
  # db.session.commit()

def add_dialogues():
  entry1 = Dialogue(username="charlie", receiver="sam1", dialogue_id=1)
  entry2 = Dialogue(username="charlie", receiver="rubina1", dialogue_id=2)
  entry3 = Dialogue(username="charlie", receiver="charlie1", dialogue_id=3)
  entry4 = Dialogue(username="charlie", receiver="ranti1", dialogue_id=4)
  entry5 = Dialogue(username="charlie", receiver="hasan1", dialogue_id=5)
  db.session.add_all([entry1, entry2, entry3, entry4, entry5])
  # db.session.commit()

def add_posts():
  entry1 = Post(user_id=6, recipe_id=1, description="A tasty Italian dish.", story="I ate this with my family.", img_url="cucina/arrabbiata_oqdsuv")
  entry2 = Post(user_id=6, recipe_id=2, description="A classic dish from Thailand.", story="Can be had with tofu instead of chicken.", img_url="cucina/pad_thai_moysxl")
  db.session.add_all([entry1, entry2])
  # db.session.commit()

def add_comments():
  entry1 = Comment(user_id=4, username='exampleUser', post_id=1, text="nice post!")
  db.session.add_all([entry1])
  # db.session.commit()
  
def create_db():

  db.drop_all()
  db.create_all()
  add_users()
  add_recipes()
  add_saved_recipes()
  # add_messages()
  add_tokens()
  add_dialogues()
  add_posts()
  add_comments()
  db.session.commit()

create_db()


