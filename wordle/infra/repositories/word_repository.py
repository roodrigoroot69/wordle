from dataclasses import dataclass

from wordle.domain.repositories.word_interface import IWordsRepository
from common.infra.models import Words

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import and_, func


@dataclass
class PostgresWordRepository(IWordsRepository):

    db: Session

    def get_active_word(self):
        word = self.db.query(Words).filter(and_(func.length(Words.word) == 5, Words.is_active == True)).first()
        return word

    def get_word(self, word):
        return self.db.query(Words).filter_by(word=word).first()

    def deactivate_word(self, word: str):
        word_to_inactive = self.get_word(word)
        if word_to_inactive:
            word_to_inactive.is_active = False
            self.db.commit()
