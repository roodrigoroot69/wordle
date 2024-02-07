from pydantic import BaseModel


class WordleRequest(BaseModel):

    word: str
