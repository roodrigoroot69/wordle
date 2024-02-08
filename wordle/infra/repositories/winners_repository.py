from dataclasses import dataclass
from typing import Dict

from sqlalchemy.orm import Session

from wordle.domain.repositories.winners_repository import IWinnersRepository
from common.infra.models import Winners

@dataclass
class PostgresWinnerRepository(IWinnersRepository):

    db: Session

    def save_winner(self, user_id: int, word: str):
        winner = Winners(user_id=user_id, word=word)
        self.db.add(winner)
        self.db.commit()
        self.db.refresh(winner)
