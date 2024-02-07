from typing import Union

from fastapi import FastAPI
from wordle.infra.rest.users.endpoints import router as user_router

app = FastAPI()

app.include_router(user_router)

