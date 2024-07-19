import pytest
from flask import Flask, request, jsonify
import json

# Import the Flask app from your main application
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_valid_endpoint(client):
    response = client.get('/ask')
    assert response.status_code != 405
    assert response.status_code == 200

def test_post_question_without_question_key(client):
    data = {'not_a_question': 'This is not a question'}
    response = client.post('/ask', data=json.dumps(data), content_type='application/json')

    # Ensure that the request fails with an appropriate status code (e.g., 400 Bad Request)
    assert response.status_code == 400