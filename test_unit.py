import pytest
from app import app, clean_text, predict_fake_or_real
from io import BytesIO

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Unit test for clean_text function
def test_clean_text():
    text = "Congratulations! You've won a $1000 gift card. Click here to claim."
    expected = "congratul youv gift card click claim"
    assert clean_text(text) == expected

# Unit test for predict_fake_or_real function
def test_predict_fake_or_real_scam():
    text = "Congratulations! You've won a $1000 gift card. Click here to claim."
    prediction = predict_fake_or_real(text)
    assert prediction == 1  # Assuming 1 means scam


# Unit test for home page route
def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Scam Detection Application' in rv.data

# Unit test for about page route
def test_about_page(client):
    rv = client.get('/about')
    assert rv.status_code == 200
    assert b'About Us' in rv.data

# Unit test for file upload route
def test_file_upload(client):
    data = {
        'fileUpload': (BytesIO(b'This is some text in a file'), 'test.txt')
    }
    rv = client.post('/scam', content_type='multipart/form-data', data=data)
    assert rv.status_code == 200
    assert b'This message (article/news) is' in rv.data


if __name__ == "__main__":
    pytest.main()