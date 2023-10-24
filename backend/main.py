from decouple import config

from fastapi import FastAPI


from motor.motor_asyncio import AsyncIOMotorClient

from contextlib import asynccontextmanager


from routers.cars import router as cars_router

DB_URL = config("DB_URL", cast=str)
DB_NAME = config("DB_NAME", cast=str)


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


app.include_router(cars_router, prefix="/cars", tags=["cars"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app")
