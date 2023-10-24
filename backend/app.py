from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from models import CarDB

car = {'brand':'Fiat', 'make':'500', 'km':4000,'cm3':2000,'price':3000,
'year':1998}

cdb = CarDB(**car)

print(jsonable_encoder(cdb))


print("hello")