import json
from datetime import datetime

from pydantic import BaseModel

from app.settings import session


class TrainData(BaseModel):
    train: int
    lat: float
    lng: float
    delay: int
    category_id: int
    station: str
    next_station: int
    LocNumber: str
    WagCount: int
    TimePlanned: datetime
    date: datetime


async def fetch_trains():
    url = "https://radar.bdz.bg/bg"

    async with session.get(url) as resp:
        content = (await resp.content.read()).decode("utf-8")

    # content = open("test.html", mode="r", encoding="utf-8").read()
    search_start = "var trains = "
    start_i = content.find(search_start)
    end_i = content[start_i:].index("]") + len(content[:start_i]) + 1

    return [TrainData(**{
        k: v
        for k, v in item.items()
        if k not in ["infoWindow", "scrollbarItem"]
    }) for item in json.loads(content[start_i+len(search_start):end_i])]
