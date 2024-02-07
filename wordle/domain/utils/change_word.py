import threading

from common.infra.database import SessionLocal
from common.infra.models import Words
from sqlalchemy.sql.expression import and_, func


db = SessionLocal()


def desactive_word():
    print("Esto se ejecutara cada 10 segundos")
    print("----------------------------------")
    word = db.query(Words).filter(and_(func.length(Words.word) == 5, Words.is_active == True)).first()
    print(word.word)
    word.is_active = False
    db.commit()
    threading.Timer(30, desactive_word).start()