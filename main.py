from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from ms_core import include_routers, conf_base_middlewares

from app import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    await settings.session.close()

application = FastAPI(
    title="BDZMS",
    version="0.1.0",
    lifespan=lifespan
)


include_routers(application, Path("app") / "routers")
conf_base_middlewares(application)
