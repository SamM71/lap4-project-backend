import pytest, sys
from . import Saved_Recipe

@pytest.fixture
def saved_recipe_test_data():
  saved_recipe = Saved_Recipe("2", "3")
  saved_recipe.id = 1
  return saved_recipe

def test_init(saved_recipe_test_data):
  saved_recipe = saved_recipe_test_data
  assert isinstance(saved_recipe, Saved_Recipe)
  assert saved_recipe.user_id == "2"

def test_repr(saved_recipe_test_data, capsys):
  saved_recipe = saved_recipe_test_data
  print(saved_recipe.__repr__())
  out, err = capsys.readouterr()
  sys.stdout.write(out)
  assert out == "Saved_Recipe(id: 1, user_id: 2, recipe_id: 3)\n"

def test_json_prop(saved_recipe_test_data):
  data = saved_recipe_test_data.json
  assert data["user_id"] == "2"
  assert data["recipe_id"] == "3"
