from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorClient

from app.commons.mongo_helpers.db import get_mongo_client
from app.commons.mongo_helpers.crud import do_insert_one
from app.backend.models.libraries import LibraryBase, LibraryOut


router = APIRouter(tags=["libraries"])


@router.post("/api/libraries/", response_model=LibraryOut)
async def create_library(library: LibraryBase, mongo_client: AsyncIOMotorClient = Depends(get_mongo_client)):
    async with await mongo_client.start_session() as s:
        result = await do_insert_one(mongo_client,
                                     s,
                                     'mbop',
                                     'users',
                                     library.dict())
        return library
