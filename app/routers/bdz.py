from fastapi import APIRouter

from app.bridges.bdz import fetch_trains, TrainData

router = APIRouter(
    tags=[""]
)

@router.get("/trains")
async def get_trains() -> list[TrainData]:
    return await fetch_trains()

