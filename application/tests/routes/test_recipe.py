from application import app, routes
import pytest

@pytest.fixture()
def client():
  return app.test_client()

def test_get_recipes(client):
  res = client.get("/recipes")
  assert b"recipes" in res.data