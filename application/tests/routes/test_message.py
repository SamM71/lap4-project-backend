from application import app, routes
import pytest

adapter = app.url_map.bind('')

@pytest.fixture()
def client():
  return app.test_client()

def test_get_messages(client):
  res = client.get("/messages")
  assert b"messages" in res.data

def test_create_message(client):
  res = client.post("/messages", json={'user_id': 50, 'username': 'bob', 'text': 2})
  assert b"messages" in res.data
  ## tests route exists but doesn't increase coverage
  func = adapter.match('/messages', method='POST')
  assert 'handle_messages' in func

def test_show_message(client):
  res = client.get('/messages/1')
  assert b"message" in res.data