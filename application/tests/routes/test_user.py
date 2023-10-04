from application import app, routes, db
import pytest

db.session.rollback()
adapter = app.url_map.bind('')

@pytest.fixture()
def client():
  return app.test_client()

def test_get_users(client):
  res = client.get("/users")
  assert b"users" in res.data

def test_create_post(client):
  res = client.post("/users", json={'safasf': 4})
  assert b"Unable to create new user" in res.data
  ## tests route exists but doesn't increase coverage
  func = adapter.match('/users', method='POST')
  assert 'handle_users' in func

def test_show_user(client):
  res = client.get('/users/500')
  assert b"User not found" in res.data

def test_update_users(client):
  res = client.patch('/users/500', json={})
  assert b"user" in res.data

def test_delete_post(client):
  res = client.delete('/users/500')
  assert b"Unable to delete user" in res.data

def test_show_user_by_username(client):
  res = client.get('/users/asfasfasf')
  assert b"User not found" in res.data

def test_register(client):
  res = client.post('/users/register', json={'username': 'bob'})
  assert b"Unable to register" in res.data

def test_register(client):
  res = client.post('/users/login', json={'username': 'bob'})
  assert b"Unable to login" in res.data

def test_get_tokens(client):
  res = client.get("/users/tokens")
  assert b"tokens" in res.data

def test_delete_token(client):
  res = client.delete("/users/tokens/1000")
  assert b"Token not found" in res.data