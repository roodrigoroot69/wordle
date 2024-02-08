from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from common.infra.auth.token import get_current_user
from common.infra.database import get_db
from wordle.app.wordle_play import WordlePlayProcessor
from common.infra.cache import redis_client
from wordle.infra.repositories.word_repository import PostgresWordRepository
from wordle.infra.repositories.winners_repository import PostgresWinnerRepository
from wordle.infra.repositories.cache_repository import RedisCacheRepository
from wordle.infra.models.wordle import WordleRequest

router = APIRouter()


@router.post("/wordle/")
def wordle_play(
    word: WordleRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    postgres_word_repository = PostgresWordRepository(db=db)
    postgres_winner_repository = PostgresWinnerRepository(db=db)
    redis_cache_repository = RedisCacheRepository(redis_client)

    result = WordlePlayProcessor(
        word_repository=postgres_word_repository,
        word=word.word,
        cache_repository=redis_cache_repository,
        winner_repository=postgres_winner_repository,
        user=current_user,
    ).execute()
    return result
