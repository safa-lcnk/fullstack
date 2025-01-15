from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config
from routers.cars import router as cars_router

DB_URL: str = config("DB_URL", cast=str)
DB_NAME: str = config("DB_NAME", cast=str)

app: FastAPI = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cars_router, prefix="/cars", tags=["cars"])

@app.on_event("startup")
async def startup_db_client() -> None:
    app.mongodb_client = AsyncIOMotorClient(DB_URL)
    app.mongodb = app.mongodb_client[DB_NAME]

@app.on_event("shutdown")
async def shutdown_db_client() -> None:
    app.mongodb_client.close()
