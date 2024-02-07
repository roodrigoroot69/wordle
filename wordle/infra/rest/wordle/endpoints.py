from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from common.infra.auth.token import get_current_user
from common.infra.database import get_db
from wordle.app.wordle_play import WordlePlayProcessor
from wordle.infra.repositories.word_repository import PostgresWordRepository
from wordle.infra.models.wordle import WordleRequest

router = APIRouter()



@router.post('/wordle/')
def wordle_play(word: WordleRequest, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    postgres_word_repository = PostgresWordRepository(db=db)
    result = WordlePlayProcessor(
        word_repository=postgres_word_repository,
        word=word.word,
        user=current_user,
    ).execute()
    return result