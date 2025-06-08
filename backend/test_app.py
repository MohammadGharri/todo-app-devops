from app import app

def test_todos():
    client = app.test_client()
    response = client.get("/api/todos")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert "id" in data[0]
    assert "title" in data[0]
    assert "done" in data[0]
