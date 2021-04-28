import pytest


@pytest.mark.auth
def test_login(test_db_session, create_single_user, client):
    # Arrange
    url = '/login'
    payload = {
        "username": "test1",
        "password": "test1"
    }
    # Act
    response = client.post(url, data=payload)
    body = response.json()
    # Assert
    assert response.status_code == 200
    assert 'access_token' in body
    assert body['token_type'] == 'bearer'


@pytest.mark.auth
def test_login_raises_incorrect_username(client):
    # Arrange
    url = '/login'
    payload = {
        "username": "test1",
        "password": "test1"
    }
    # Act
    response = client.post(url, data=payload)
    body = response.json()
    # Assert
    assert response.status_code == 404
    assert body['detail'] == 'Incorrect Username'


@pytest.mark.auth
def test_login_raises_incorrect_password(create_single_user, client):
    # Arrange
    url = '/login'
    payload = {
        "username": "test1",
        "password": "wrong password"
    }
    # Act
    response = client.post(url, data=payload)
    body = response.json()
    # Assert
    assert response.status_code == 404
    assert body['detail'] == 'Incorrect Password'