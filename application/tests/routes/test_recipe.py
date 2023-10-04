from application import app, routes
import pytest
import json

adapter = app.url_map.bind('')

@pytest.fixture()
def client():
  return app.test_client()

def test_get_recipes(client):
  res = client.get("/recipes")
  assert b"recipes" in res.data

def test_create_recipe(client):
  # res = client.post('/recipes', json={
  #     "user_id": 1,
  #     "name": "recipe1",
  #     "culture": "a culture",
  #     "ingredients": [
  #       {
  #         "ingredient": "ingredient1",
  #         "amount": "500g"
  #       }
  #     ],
  #     "steps": [
  #       {
  #         "step": "first step"
  #       }
  #     ],
  #     "description": "example recipe",
  #     "img_url": "cucina/food_vbd3ll"
  #   })
  # assert 'first step' in str(res.data)
  res = client.post('/recipes', json={'user_id': 1})
  assert b"Unable to create new recipe" in res.data
  ## tests route exists but doesn't increase coverage
  func = adapter.match('/recipes', method='POST')
  assert 'handle_recipes' in func

def test_show_recipe(client):
  res = client.get('/recipes/1')
  assert b"recipe" in res.data

def test_update_recipe(client):
  res = client.patch('/recipes/1', json={})
  assert b"recipe" in res.data

def test_delete_recipe(client):
  res = client.delete('/recipes/3000')
  assert b"Unable to delete recipe" in res.data

def test_show_recipe_by_name(client):
  res = client.get('recipes/recipe1')
  assert b"example recipe" in res.data