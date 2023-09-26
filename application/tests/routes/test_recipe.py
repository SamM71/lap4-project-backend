from application import app, routes
import pytest

@pytest.fixture()
def client():
  return app.test_client()

def test_get_recipes(client):
  res = client.get("/recipes")
  print(res)
  print(res.data)
  assert b"recipes" in res.data