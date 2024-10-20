import logging
import sys
import uvicorn
from config import get_settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import PostgresDsn
from routes.router import central_router
from sqlalchemy.pool import NullPool
from fastapi_async_sqlalchemy import SQLAlchemyMiddleware
import asyncpg

logging.basicConfig(handlers=[logging.StreamHandler(sys.stdout)], level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Koloni Notification Service",
    version="0.1.0",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.include_router(central_router, prefix="/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
)

app.add_middleware(
    SQLAlchemyMiddleware,
    db_url=PostgresDsn.build(
        scheme="postgresql+asyncpg",
        user=get_settings().database_user,
        password=get_settings().database_password,
        host=get_settings().database_host,
        port=str(get_settings().database_port),
        path=f"/{get_settings().database_name}",
    ),
    engine_args={
        "echo": False,
        "pool_pre_ping": True,
        "pool_recycle": 1800,
        "poolclass": NullPool,
    },
)


async def create_pool():
    db_params = {
        "user": get_settings().database_user,
        "password": get_settings().database_password,
        "host": get_settings().database_host,
        "port": str(get_settings().database_port),
        "database": get_settings().database_name,
    }

    pool: asyncpg.Pool = await asyncpg.create_pool(
        **db_params, min_size=2, max_size=500
    )

    return pool

@app.on_event("startup")
async def startup_event():
    app.state.pool = await create_pool()

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=get_settings().host,
        port=get_settings().port,
        access_log=True,
        reload=True,
    )
