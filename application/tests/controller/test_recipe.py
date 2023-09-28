from application import app
import pytest
from flask import jsonify
from ...controllers.recipe import index
from ...models.Recipe import Recipe

@pytest.fixture
def recipe_test_data():
  recipe1 = Recipe(4, 'test recipe', 'test culture', ['ing1', 'ing2'], ['step1', 'step2'], 'desc1', 'url1')
  recipe1.id = 1
  recipe2 = Recipe(3, 'test recipe 2', 'test culture 2', ['ing1', 'ing2'], ['step1', 'step2'], 'desc2', 'url2')
  recipe2.id = 2
  return [recipe1, recipe2]


def test_index(monkeypatch, recipe_test_data):
  class MockQuery:
    @staticmethod
    def all():
      return recipe_test_data
    
  monkeypatch.setattr(Recipe, 'query', MockQuery())
  res = index()
  data = res.json
  assert 'recipes' in data
  assert 'test recipe' in str(data)
  assert 'desc1' in str(data)
  assert res.status_code == 200
    
  