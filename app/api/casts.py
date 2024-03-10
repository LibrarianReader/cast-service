from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import CastOut, CastIn, CastUpdate
from app.api import db_manager

casts = APIRouter()

@casts.post('/', response_model=CastOut, status_code=201) #localhost:8002/api/v1/casts 
async def create_cast(payload: CastIn):
    cast_id = await db_manager.add_cast(payload)

    response = {
        'id': cast_id,
        **payload.dict()
    }

    return response


@casts.get('/', response_model=List[CastOut]) #localhost:8001/api/v1/animes
async def get_casts():
    return await db_manager.get_all_cast()