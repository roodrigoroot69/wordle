from common.infra.database import Base
from common.infra.time_utils import now

from sqlalchemy import (
    Column,
    DateTime,
    TIMESTAMP,
    String,
    Integer,
    ForeignKey,
    LargeBinary,
    Boolean,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class BaseModel(Base):

    __abstract__ = True

    created_at = Column(DateTime, default=now)
    updated_at = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp()
    )


class Words(BaseModel):

    __tablename__ = "words"

    id = Column(Integer, primary_key=True)
    word = Column(String)
    is_active = Column(Boolean, default=True)


class User(BaseModel):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    winners = relationship("Winners", back_populates="user")


class Winners(BaseModel):

    __tablename__ = "winners"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="winners")
    word = Column(String)
