import pytest
from app.main import create_app
from flask import Flask

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_process_file(client):
    response = client.post('/process')
    assert response.status_code == 400
    assert b"Aucun fichier trouv" in response.data
