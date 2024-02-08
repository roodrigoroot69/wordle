from dataclasses import dataclass

from wordle.domain.repositories.word_interface import IWordsRepository
from common.infra.models import Words

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import and_, func


LENGTH_WORD_ALLOWED = 5


@dataclass
class PostgresWordRepository(IWordsRepository):

    db: Session

    def get_active_word(self):
        word = (
            self.db.query(Words)
            .filter(
                and_(
                    func.length(Words.word) == LENGTH_WORD_ALLOWED,
                    Words.is_active == True,
                )
            )
            .first()
        )
        return word
