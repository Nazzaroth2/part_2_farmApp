# needed for parallel package importing
# import sys
# sys.path.append(r'G:\Arbeit_Active\Programming\FARM_Book_Project\part_2_FullStackApp')

from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr
from pydantic_core import core_schema
from pydantic.json_schema import JsonSchemaValue
from typing import Optional, Annotated, Any
from email_validator import validate_email, EmailNotValidError

from .mongo_base import MongoBaseModel


class CarBase(MongoBaseModel):
    brand: str = Field(..., min_length=3)
    make: str = Field(..., min_length=3)
    year: int = Field(..., gt=1975, lt=2023)
    price: int = Field(...)
    km: int = Field(...)
    cm3: int = Field(..., gt=600, lt=8000)


class CarUpdate(BaseModel):
    price: Optional[int] = None


class CarDB(CarBase):
    owner: str = Field(...)
