from fastapi import FastAPI
from wordle.infra.rest.users.endpoints import router as user_router
from wordle.infra.rest.wordle.endpoints import router as wordle_router


app = FastAPI()

app.include_router(user_router)
app.include_router(wordle_router)
