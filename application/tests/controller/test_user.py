from application.models import User
import pytest
from application.controllers.user import index, show
import json
import logging

@pytest.fixture
def mock_user_data():
    user1 = User(username='username1', email='email1', name='user1', password='password1')
    user1.id = 1
    user2 = User(username='username2', email='email2', name='user2', password='password2')
    user2.id = 2
    return [user1, user2]



def test_index(monkeypatch, mock_user_data):

    class MockQuery:
        @staticmethod
        def all():
            return mock_user_data

    monkeypatch.setattr(User, 'query', MockQuery())

    response = index()

    expected_json = {'users': [{'id': 1, 'username': 'username1', 'email': 'email1', 'name': 'user1', 'password': 'password1'},
                               {'id': 2, 'username': 'username2', 'email': 'email2', 'name': 'user2', 'password': 'password2'}]}
    
    assert response.status_code == 200
    assert response.json == expected_json


