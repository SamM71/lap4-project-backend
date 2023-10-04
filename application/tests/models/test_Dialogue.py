import pytest, sys
from ...models.Dialogue import Dialogue

@pytest.fixture
def dialogue_test_data():
  dialogue = Dialogue('bob', 'bob2', 5)
  dialogue.id = 5
  return dialogue

def test_init(dialogue_test_data):
  dialogue = dialogue_test_data
  assert isinstance(dialogue, Dialogue)
  assert dialogue.username == "bob"

def test_repr(dialogue_test_data, capsys):
  dialogue = dialogue_test_data
  print(dialogue.__repr__())
  out, err = capsys.readouterr()
  sys.stdout.write(out)
  assert "username" in out
  assert out == "Dialogue(id: 5, username: bob, receiver: bob2)\n"
