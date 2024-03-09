from fastapi.testclient import TestClient
from app.main import app
from app.api.models import CastIn, CastOut, CastUpdate


client = TestClient(app)

cast_data = {
    'name': 'Name',
    'nationality': 'Country',
}

def test_create_cast():
    cast = CastIn(**cast_data)
    assert dict(cast) == cast_data

def test_update_cast_name():
    cast = CastIn(**cast_data)
    cast_upd = CastUpdate(name='New Name', **cast_data)
    assert dict(cast_upd) == {'name': 'New Name', 'nationality': 'Country'}

def test_update_cast_nationality():
    cast = CastIn(**cast_data)
    cast_upd = CastUpdate(nationality='New Country', **cast_data)
    assert dict(cast_upd) == {'name': 'Name', 'nationality': 'New Country'}

'''
def create_cast_success():
    data = {
        "name": "string",
        "nationality": "string"
    }
    response = client.post("/api/v1/casts/", json=data, headers={"accept": "application/json", "Content-Type": "application/json"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

def create_cast_failure():
    data = {}
    response = client.post("/api/v1/casts/", json=data, headers={"accept": "application/json", "Content-Type": "application/json"})
    assert response.status_code == 422

def test_get_cast_success():
    response = client.get("/api/v1/casts/1/", headers={"accept": "application/json"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

def test_get_cast_failure():
    response = client.get("/api/v1/casts/999/", headers={"accept": "application/json"})
    assert response.status_code == 404
'''