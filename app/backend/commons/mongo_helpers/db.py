from motor.motor_asyncio import AsyncIOMotorClient


class DataBase():
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_mongo_client() -> AsyncIOMotorClient:
    return db.client