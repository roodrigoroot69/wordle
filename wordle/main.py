import threading

from fastapi import FastAPI
from wordle.infra.rest.users.endpoints import router as user_router
from wordle.infra.rest.wordle.endpoints import router as wordle_router
from wordle.domain.utils.change_word import desactive_word


app = FastAPI()

desactive_word()

app.include_router(user_router)
app.include_router(wordle_router)
