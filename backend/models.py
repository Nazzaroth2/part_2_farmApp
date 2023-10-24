from bson import ObjectId
from pydantic import BaseModel, Field, ConfigDict, GetJsonSchemaHandler
from pydantic_core import core_schema
from pydantic.json_schema import JsonSchemaValue
from pydantic.functional_validators import AfterValidator
from typing import Optional, Annotated, Any, Callable

# new uptodate pydantic-v2 way of validating mongoDB ObjectId
class ObjectIdPydanticAnnotation:
    @classmethod
    def validate_object_id(cls, v: Any, handler) -> ObjectId:
        if isinstance(v, ObjectId):
            return v

        s = handler(v)
        if ObjectId.is_valid(s):
            return ObjectId(s)
        else:
            raise ValueError("Invalid ObjectId")

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, _handler) -> core_schema.CoreSchema:
        assert source_type is ObjectId
        return core_schema.no_info_wrap_validator_function(
            cls.validate_object_id, 
            core_schema.str_schema(), 
            serialization=core_schema.to_string_ser_schema(),
        )

    @classmethod
    def __get_pydantic_json_schema__(cls, _core_schema, handler) -> JsonSchemaValue:
        return handler(core_schema.str_schema())
    

class MongoBaseModel(BaseModel):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation] = Field(default_factory=ObjectId, alias="_id")

    class Config:
        json_encoders = {ObjectId: str}


entry = MongoBaseModel()
print(entry.id)


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




# from typing_extensions import Annotated
# from pydantic import BaseModel 
# from pydantic.functional_validators import AfterValidator 
# from bson import ObjectId as _ObjectId 

