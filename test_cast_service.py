import pytest
from app.api.models import CastIn, CastOut, CastUpdate

cast = CastIn(
    name='Bred Pitt',
    nationality='Russian'
)


def test_create_cast(cast: CastIn = cast):
    assert dict(cast) == {'name': cast.name,
                          'nationality': cast.nationality}


def test_update_cast_title(cast: CastIn = cast):
    cast_upd = CastOut(
        name='Bred Pitt',
        nationality=cast.nationality,
        id=1
    )
    assert dict(cast_upd) == {'name': cast.name,
                              'nationality': cast.nationality,
                              'id': cast_upd.id
                              }


def test_update_cast_genre(cast: CastIn = cast):
    cast_upd = CastOut(
        name=cast.name,
        nationality=cast.nationality,
        id=1
    )
    assert dict(cast_upd) == {'name': cast.name,
                              'nationality': cast.nationality,
                              'id': cast_upd.id}
