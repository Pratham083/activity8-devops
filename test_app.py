# test_app.py
import app


def test_hello():
    client = app.app.test_client()
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}


def test_echo():
    client = app.app.test_client()
    payload = {"msg": "ping"}
    response = client.post('/echo', json=payload)
    assert response.status_code == 201
    assert response.get_json() == payload


def test_put():
    client = app.app.test_client()
    payload = {"msg": "updating"}
    response = client.put('/put', json=payload)
    assert response.status_code == 200
    assert response.get_json() == payload


def test_delete():
    client = app.app.test_client()
    response = client.delete('/delete')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Deleted"}
