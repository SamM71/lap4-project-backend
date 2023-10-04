from application import app, routes
import pytest

adapter = app.url_map.bind('')

@pytest.fixture()
def client():
  return app.test_client()

def test_get_dialogues(client):
  res = client.get("/dialogues")
  assert b"dialogues" in res.data

def test_create_dialogue(client):
  res = client.post("/dialogues", json={'user_id': 300, 'username': 'bob', 'receiver': 1})
  assert b"dialogue" in res.data
  ## tests route exists but doesn't increase coverage
  func = adapter.match('/dialogues', method='POST')
  assert 'handle_dialogue' in func

def test_show_dialogue(client):
  res = client.get('/dialogues/1')
  assert b"dialogue" in res.data