from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from app.configdb import SessionLocal, Base
from app.schema import PelangganSchema, PemesananSchema
import app.routers.crud as crud
from app.routers.routes import router
from .routers import routes, crud, auth, user


app = FastAPI()

# Menambahkan router yang telah dibuat sebelumnya
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(routes.router)

# Inisialisasi database
Base.metadata.create_all(bind=crud.engine)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)