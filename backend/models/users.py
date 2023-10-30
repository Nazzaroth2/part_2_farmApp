from enum import Enum
from typing import Optional, Annotated, Any

from pydantic import BaseModel, Field, EmailStr, validator
from pydantic_core import core_schema
from pydantic.json_schema import JsonSchemaValue
from email_validator import validate_email, EmailNotValidError

from .mongo_base import MongoBaseModel


class Role(str, Enum):
    SALESPERSON = "SALESPERSON"
    ADMIN = "ADMIN"


class UserBase(MongoBaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    email: str = Field(...)
    password: str = Field(..., min_length=8)
    role: Role

    @validator("email")
    def valid_email(cls, value):
        try:
            # get normalized email form from email_validator
            email = validate_email(value).email
            return email
        except EmailNotValidError as e:
            raise EmailNotValidError


class LoginBase(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)


class CurrentUser(BaseModel):
    email: EmailStr = Field(...)
    username: str = Field(...)
    role: Role = Field(...)
