import pytest, sys
from ...models.Token import Token

@pytest.fixture
def token_test_data():
    token = Token("2", "jhcbdvsdhvsdnbhdvjhbhd")
    token.id = 1
    return token

def test_init(token_test_data):
    token = token_test_data
    assert isinstance(token, Token)
    assert token.user_id == "2"
    assert token.token == "jhcbdvsdhvsdnbhdvjhbhd"

def test_repr(token_test_data, capsys):
    token = token_test_data
    print(token.__repr__())
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    out_stripped = out.strip()
    assert "jhcbdvsdhvsdnbhdvjhbhd" in out_stripped
    assert out_stripped == "Token(id: 1, user_id: 2, token: jhcbdvsdhvsdnbhdvjhbhd)"

def test_json_prop(token_test_data):
    data = token_test_data.json
    assert data["user_id"] == "2"
    assert data["token"] == "jhcbdvsdhvsdnbhdvjhbhd"
