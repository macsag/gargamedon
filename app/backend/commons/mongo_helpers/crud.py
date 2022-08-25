from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession


async def do_insert_one(
        mongo_client: AsyncIOMotorClient,
        session: AsyncIOMotorClientSession,
        db_to_get: str,
        collection_to_get: str,
        document: dict
        ):

    db = mongo_client[db_to_get]
    collection = db[collection_to_get]

    result = await collection.insert_one(document, session=session)
    return result
