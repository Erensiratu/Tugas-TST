from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from config import SessionLocal, Base
from schema import PelangganSchema, PemesananSchema
import crud
from routes import router

app = FastAPI()

# Menambahkan router yang telah dibuat sebelumnya
app.include_router(router)

# Inisialisasi database
Base.metadata.create_all(bind=crud.engine)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)