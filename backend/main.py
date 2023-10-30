import os

# make sure /backend is working directory
main_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_directory)


from decouple import config

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from motor.motor_asyncio import AsyncIOMotorClient

from contextlib import asynccontextmanager

from routers.cars import router as cars_router
from routers.users import router as users_router

# DB_URL = config("DB_URL_SERVER", cast=str)
DB_URL = config("DB_URL_LOCAL", cast=str)
DB_NAME = config("DB_NAME", cast=str)

# origins = [
#     "http://localhost",
#     "http://localhost:8080",
#     "http://localhost:3000",
#     "http://localhost:8000",
# ]
origins = ["*"]


# new fastapi system for startup and shutdown with lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup-code
    app.mongodb_client = AsyncIOMotorClient(DB_URL)
    app.mongodb = app.mongodb_client[DB_NAME]

    yield

    # shutdown-code
    app.mongodb_client.close()


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(cars_router, prefix="/cars", tags=["cars"])
app.include_router(users_router, prefix="/users", tags=["users"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app")
