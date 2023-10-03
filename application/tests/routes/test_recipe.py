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

def test_post(client):

  res = client.post('/recipes', json={
      "user_id": 1,
      "name": "recipe1",
      "culture": "a culture",
      "ingredients": [
          {
            "ingredient": "ingredient1",
            "amount": "500g"
          }
      ],
      "steps": [
          {
              "step": "first step"
          }
      ],
      "description": "example recipe",
      "img_url": "cucina/food_vbd3ll"
    })
  func = adapter.match('/recipes', method='POST')
  assert 'handle_recipes' in func
  assert 'first step' in str(res.data)