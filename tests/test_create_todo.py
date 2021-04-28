import pytest


@pytest.mark.todos
def test_create_new_todo(login, client):
    # Arrange
    url = '/create-todo'
    payload = {
        "title": "Buy Milk",
        "complete": False
    }
    headers = {
        "Authorization": f"Bearer {login['access_token']}"
    }
    # Act
    response = client.post(url, headers=headers, json=payload)
    body = response.json()
    # Assert
    assert response.status_code == 200
    assert body['title'] == 'Buy Milk'
    assert body['complete'] == False
    assert body['id'] == 1
    assert body['owner_id'] == 1
