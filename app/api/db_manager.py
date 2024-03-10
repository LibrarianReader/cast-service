from app.api.models import CastIn, CastOut, CastUpdate
from app.api.db import casts, database


async def add_cast(payload: CastIn):
    query = casts.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_all_cast():
    query = casts.select()
    return await database.fetch_all(query=query)
