import pytest, sys
from ...models.Post import Post

@pytest.fixture
def post_test_data():
  post = Post(3, 2, "my description", "my story", "testurl")
  post.id = 5
  return post

def test_init(post_test_data):
  post = post_test_data
  assert isinstance(post, Post)
  assert post.img_url == "testurl"

def test_repr(post_test_data, capsys):
  post = post_test_data
  print(post.__repr__())
  out, err = capsys.readouterr()
  sys.stdout.write(out)
  assert "user_id" in out
  assert out == "Post(id: 5, user_id: 3, recipe_id: 2)\n"

def test_json_prop(post_test_data):
  data = post_test_data.json
  assert data["description"] == "my description"
  assert data["story"] == "my story"
