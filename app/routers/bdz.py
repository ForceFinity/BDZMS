from typing import Annotated

from fastapi import APIRouter, HTTPException, BackgroundTasks
# from fastapi.params import Depends, Query
# from starlette import status
# from tortoise.contrib.postgres.functions import Random
#
# from app import QuestionSchema, QuestionComplexCreate, QuestionCRUD, QuestionCreate, Answer, Question, QuestionsDone
from app.bridges.bdz import fetch_trains, TrainData

# from app.bridges.dependencies import get_current_user, get_current_admin
# from app.bridges.users import UserSchema, UsersBridge

router = APIRouter(
    tags=[""]
)

@router.get("/trains")
async def get_trains() -> list[TrainData]:
    return await fetch_trains()

