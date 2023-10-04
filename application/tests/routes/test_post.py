from application import app, routes
import pytest

adapter = app.url_map.bind('')

@pytest.fixture()
def client():
  return app.test_client()

def test_get_post(client):
  res = client.get("/posts")
  assert b"posts" in res.data

def test_create_post(client):
  res = client.post("/posts", json={'user_id': 4})
  assert b"Unable to create new post" in res.data
  ## tests route exists but doesn't increase coverage
  func = adapter.match('/posts', method='POST')
  assert 'handle_posts' in func

def test_show_post(client):
  res = client.get('/posts/50')
  assert b"Post not found" in res.data

def test_update_post(client):
  res = client.patch('/posts/50', json={})
  assert b"post" in res.data

def test_delete_post(client):
  res = client.delete('/posts/50')
  assert b"Unable to delete post" in res.data