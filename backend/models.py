from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional

class PyObjectID(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid():
            raise ValueError("Invalid objectid")
        return ObjectId(v)
    
    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")

    
class MongoBaseModel(BaseModel):
    id: PyObjectID = Field(default_factory=PyObjectID, alias="_id")

    class Config:
        json_encoders = {ObjectId: str}


class CarBase(MongoBaseModel):
    brand: str = Field(..., min_length=3)
    make: str = Field(..., min_length=3)
    year: int = Field(...)
    price: int = Field(...)
    km: int = Field(...)
    cm3: int = Field(...)


class CarUpdate(MongoBaseModel):
    price: Optional[int] = None


class CarDB(CarBase):
    pass