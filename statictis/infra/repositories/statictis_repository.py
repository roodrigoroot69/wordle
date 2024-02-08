from dataclasses import dataclass

from statictis.domain.repositories.statictis_repository import IStatictisRepository
from common.infra.models import Winners, User

from sqlalchemy import func
from sqlalchemy.orm import Session


@dataclass
class PostgresStatictisRepository(IStatictisRepository):

    db: Session

    def get_most_accurate_words(self):
        return (
            self.db.query(Winners.word, func.count().label("repetition_count"))
            .group_by(Winners.word)
            .having(func.count() > 2)
            .order_by(func.count().desc())
        ).all()


    def get_bast_ten_players(self):
        return (
            self.db.query(User.username, func.count().label('most_words'))
            .join(Winners, Winners.user_id == User.id)
            .group_by(User.username, Winners.user_id)
            .order_by(func.count().desc())
            .limit(10)
        ).all()
