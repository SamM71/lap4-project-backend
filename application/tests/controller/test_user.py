from application.models import User
import pytest
from application.controllers.user import index 
# import json

class MockUser:
    def __init__(self, username, email, name, password):
        self.username = username
        self.email = email
        self.name = name
        self.password = password

def test_index(monkeypatch):
    user_data = [{'username':'username1', 'email':'email1', 'name':'user1', 'password':'password1'}, {'username':'username2', 'email':'email2', 'name':'user2', 'password':'password2'}]

    users = [MockUser(**data) for data in user_data]

    def mock_query_all():
        return users
    
    monkeypatch.setattr(User.query, 'all', mock_query_all)

    response = index()

    assert response.status_code == 200
    assert response.json == {'users': user_data}  #NOT PASSING!!!
