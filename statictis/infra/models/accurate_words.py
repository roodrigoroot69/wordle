from typing import List

from pydantic import BaseModel

class ResultItem(BaseModel):
    name: str
    count: int

class ResultResponse(BaseModel):
    results: List[ResultItem]
