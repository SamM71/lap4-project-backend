import pytest, sys
from . import Recipe

@pytest.fixture
def recipe_test_data():
  recipe = Recipe("3", "testrecipe", "testculture", "A wonderful recipe", "testurl")
  recipe.id = 5
  return recipe

def test_init(recipe_test_data):
  recipe = recipe_test_data
  assert isinstance(recipe, Recipe)
  assert recipe.name == "testrecipe"

def test_repr(recipe_test_data, capsys):
  recipe = recipe_test_data
  print(recipe.__repr__())
  out, err = capsys.readouterr()
  sys.stdout.write(out)
  assert "testrecipe" in out
  assert out == "Recipe(id: 5, user_id: 3, name: testrecipe)\n"

def test_json_prop(recipe_test_data):
  data = recipe_test_data.json
  assert data["description"] == "A wonderful recipe"
  assert data["name"] == "testrecipe"
