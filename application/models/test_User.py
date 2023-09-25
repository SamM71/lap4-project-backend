import pytest, sys
from . import User

@pytest.fixture
def user_test_data():
  user = User("testuser", "test@example.com", "Test", "jkljkl")
  user.id = 8
  return user

def test_init(user_test_data):
  user = user_test_data
  assert isinstance(user, User)
  assert user.username == "testuser"

def test_repr(user_test_data, capsys):
  user = user_test_data
  print(user.__repr__())
  out, err = capsys.readouterr()
  sys.stdout.write(out)
  assert "testuser" in out
  assert out == "User(id: 8, username: testuser)\n"

def test_json_prop(user_test_data, capsys):
  data = user_test_data.json
  assert data["email"] == "test@example.com"
  assert data["name"] == "Test"
