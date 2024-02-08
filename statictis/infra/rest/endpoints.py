from fastapi import APIRouter, Depends
from common.infra.auth.token import get_current_user
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from statictis.app.best_players import GetBestPlayersProcessor
from statictis.app.accurate_words import AccurateWordsProcessor
from common.infra.database import get_db
from statictis.infra.repositories.statictis_repository import (
    PostgresStatictisRepository,
)
from statictis.infra.models.accurate_words import ResultItem, ResultResponse
from statictis.infra.models.best_ten_players import WinnersModel, WinnersResponse

router = APIRouter()


@router.get("/accurate_words/", status_code=200)
def get_accurate_Words(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    postgres_statictis_repository = PostgresStatictisRepository(db=db)
    accurate_words = AccurateWordsProcessor(
        statictis_repository=postgres_statictis_repository
    ).execute()

    result = [ResultItem(name=name, count=count) for name, count in accurate_words]
    return JSONResponse(content=ResultResponse(results=result).dict())


@router.get("/best_players/", status_code=200)
def get_accurate_Words(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):

    postgres_statictis_repository = PostgresStatictisRepository(db=db)
    get_best_players = GetBestPlayersProcessor(
        statictis_repository=postgres_statictis_repository
    ).execute()

    result = [WinnersModel(username=username, victories=victories) for username, victories in get_best_players]
    return JSONResponse(content=WinnersResponse(results=result).dict())

