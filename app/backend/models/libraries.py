from typing import List

from app.backend.models.mongo_models import MongoModel


class LibraryBase(MongoModel):
    library_owner: str
    email: str
    role: str
    street: str
    street_number: str
    flat_number: str
    postal_code: str
    radius: int


class LibraryOut(UserBase):
    id: str