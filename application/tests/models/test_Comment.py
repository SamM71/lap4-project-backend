import pytest, sys
from ...models.Comment import Comment
from datetime import datetime

@pytest.fixture
def comment_test_data():
  comment = Comment(3, 2, "my comment")
  comment.id = 5
  comment.time_posted = datetime.now()
  return comment

def test_init(comment_test_data):
  comment = comment_test_data
  assert isinstance(comment, Comment)
  assert comment.text == "my comment"

def test_repr(comment_test_data, capsys):
  comment = comment_test_data
  print(comment.__repr__())
  out, err = capsys.readouterr()
  sys.stdout.write(out)
  assert "user_id" in out
  assert out == "Comment(id: 5, user_id: 3, post_id: 2)\n"

def test_json_prop(comment_test_data):
  data = comment_test_data.json
  assert data["text"] == "my comment"
  assert data["post_id"] == 2