from typing import Union

from fastapi import FastAPI

from statictis.infra.rest.endpoints import router as statictis_router

app = FastAPI()
app.include_router(statictis_router)
