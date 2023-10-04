from application import app, routes
import pytest

adapter = app.url_map.bind('')

@pytest.fixture()
def client():
  return app.test_client()

def test_get_comments(client):
  res = client.get("/posts/50/comments")
  assert b"comments" in res.data

def test_create_comment(client):
  res = client.post("/posts/50/comments", json={'user_id': 4})
  assert b"Unable to create new comment" in res.data
  ## tests route exists but doesn't increase coverage
  func = adapter.match('/posts/50/comments', method='POST')
  assert 'handle_comments' in func

def test_show_comment(client):
  res = client.get('/posts/50/comments/50')
  assert b"comment" in res.data

def test_update_comment(client):
  res = client.patch('/posts/50/comments/50', json={})
  assert b"comment" in res.data

def test_delete_comment(client):
  res = client.delete('/posts/50/comments/50')
  assert b"Unable to delete comment" in res.data