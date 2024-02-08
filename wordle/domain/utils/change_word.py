import threading

from common.infra.database import SessionLocal
from common.infra.models import Words
from common.infra.cache import redis_client

from sqlalchemy.sql.expression import and_, func


db = SessionLocal()
EXPIRATION_TIME = 300


def desactive_word():
    word = (
        db.query(Words)
        .filter(and_(func.length(Words.word) == 5, Words.is_active == True))
        .first()
    )
    word.is_active = False
    db.commit()
    redis_client.flushall()
    threading.Timer(EXPIRATION_TIME, desactive_word).start()
