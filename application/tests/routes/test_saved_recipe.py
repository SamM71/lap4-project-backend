from application import app, routes
import pytest
import json

adapter = app.url_map.bind('')

@pytest.fixture()
def client():
  return app.test_client()

def test_get_srecipes(client):
  res = client.get("/saved/4")
  assert b"recipe" in res.data

def test_create_srecipe(client):
  res = client.post('/saved/1000/1000')
  assert b"Unable to save recipe" in res.data
  ## tests route exists but doesn't increase coverage
  func = adapter.match('/recipes', method='POST')
  assert 'handle_recipes' in func

def test_delete_srecipe(client):
  res = client.delete('/saved/1000/1000')
  assert b"Unable to delete recipe" in res.data