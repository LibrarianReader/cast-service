from app.main import app
from app.api.models import CastIn, CastOut, CastUpdate


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