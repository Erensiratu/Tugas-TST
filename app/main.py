from fastapi import FastAPI
from routes import router
from config import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/api", tags=["api"])
