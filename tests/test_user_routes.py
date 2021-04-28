import pytest


@pytest.mark.users
def test_create_new_user(test_db_session, client):
    # Arrange
    url = '/create-user'
    payload = {
        "username": "test1",
        "password": "test1"
    }
    # Act
    response = client.post(url, json=payload)
    body = response.json()
    # Assert
    assert response.status_code == 200
    assert body['username'] == 'test1'
    assert len(body['todos']) == 0


@pytest.mark.users
def test_create_user_raises_username_taken(test_db_session, create_single_user, client):
    # Arrange
    url = '/create-user'
    payload = {
        "username": "test1",
        "password": "test1"
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
