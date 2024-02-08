from dataclasses import dataclass

from statictis.domain.repositories.statictis_repository import IStatictisRepository
from common.infra.models import Winners

from sqlalchemy import func
from sqlalchemy.orm import Session


@dataclass
class PostgresStatictisRepository(IStatictisRepository):

    db: Session

    def get_most_accurate_words(self):
        return (
            self.db.query(Winners.word, func.count().label('repetition_count'))
            .group_by(Winners.word)
            .having(func.count() > 2)
            .order_by(func.count().desc())
        ).all()
