import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Scam Detection Application' in rv.data

def test_predict_scam(client):
    rv = client.post('/text', data=dict(
        textInput="Congratulations! You've won a $1000 gift card. Click here to claim."
    ))
    assert rv.status_code == 200
    assert b'This message (article/news) is a scam Text.' in rv.data

def test_predict_real(client):
    rv = client.post('/text', data=dict(
        textInput="Let's meet up for lunch tomorrow at 1 PM."
    ))
    assert rv.status_code == 200
    assert b'This message (article/news) is a Real Text.' in rv.data

def test_default_theme(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Scam Detection Application' in rv.data

def test_black_theme(client):
    rv = client.post('/apply_theme', data=dict(
        theme='black'
    ))
    assert rv.status_code == 200
    assert b'{"status":"success"}' in rv.data
