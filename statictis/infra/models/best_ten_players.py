from typing import List

from pydantic import BaseModel


class WinnersModel(BaseModel):
    username: str
    victories: int


class WinnersResponse(BaseModel):
    results: List[WinnersModel]
