import pytest


@pytest.mark.users
def test_create_new_user(test_db_session, credentials, client):
    # Arrange
    url = '/create-user'
    payload = {
        "username": credentials.get("username"),
        "password": credentials.get("password")
    }

    # Act
    response = client.post(url, json=payload)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert body['username'] == credentials.get("username")
    assert len(body['todos']) == 0


@pytest.mark.users
def test_create_user_raises_username_taken(test_db_session, create_single_user, credentials, client):
    # Arrange
    url = '/create-user'
    payload = {
        "username": credentials.get("username"),
        "password": credentials.get("password")
    }

    # Act
    response = client.post(url, json=payload)
    body = response.json()

    # Assert
    assert response.status_code == 409
    assert body['detail'] == 'Username Taken'


@pytest.mark.users
def test_get_user(create_single_user, client):
    # Arrange
    url = '/get-user/1'

    # Act
    response = client.get(url)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert 1 == body['id']
    assert 1 is body['id']


@pytest.mark.users
def test_get_user_raises_user_not_found(client):
    # Arrange
    url = '/get-user/1120398'

    # Act
    response = client.get(url)
    body = response.json()

    # Assert
    assert response.status_code == 400
    assert 'User Not Found' in body['detail']


@pytest.mark.users
def test_delete_user(login, client):
    # Arrange
    url = '/delete-user'
    headers = {
        "Authorization": f"Bearer {login['access_token']}"
    }
    # Act
    response = client.delete(url, headers=headers)
    body = response.json()
    # Assert
    assert response.status_code == 200
    assert body["message"] == "User Successfully Deleted"


@pytest.mark.users
def test_delete_user_raises_not_authenticated(client):
    # Arrange
    url = '/delete-user'
    # Act
    response = client.delete(url)
    body = response.json()
    # Assert
    assert response.status_code == 401
    assert body["detail"] == "Not authenticated"
