from fastapi import APIRouter, HTTPException, Depends, Path
from sqlalchemy.orm import Session
from schema import PelangganSchema, PemesananSchema, PelangganListSchema, PemesananListSchema
import crud
from config import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#PELANGGAN
@router.get("/pelanggan/", response_model=PelangganListSchema)
async def get_all_pelanggan(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    pelanggan = crud.get_all_pelanggan(db, skip, limit)
    return {"data": pelanggan}

@router.get("/pelanggan/{pelanggan_id}", response_model=PelangganSchema)
async def get_pelanggan(db: Session = Depends(get_db), pelanggan_id: int = Path(..., title="Pelanggan ID")):
    pelanggan = crud.get_pelanggan(db, pelanggan_id)
    if pelanggan is None:
        raise HTTPException(status_code=404, detail="Pelanggan not found")
    return pelanggan

@router.post("/pelanggan/", response_model=PelangganSchema)
async def create_pelanggan(pelanggan: PelangganSchema, db: Session = Depends(get_db)):
    return crud.create_pelanggan(db, pelanggan)

@router.put("/pelanggan/{id}", response_model=PelangganSchema)
async def update_pelanggan(id: int, updated_pelanggan: PelangganSchema, db: Session = Depends(get_db)):
    pelanggan = crud.update_pelanggan(db, id, updated_pelanggan)
    if pelanggan is None:
        raise HTTPException(status_code=404, detail="Pelanggan not found")
    return pelanggan

@router.delete("/pelanggan/{pelanggan_id}", response_model=PelangganSchema)
async def remove_pelanggan(pelanggan_id: int, db: Session = Depends(get_db)):
    pelanggan = crud.remove_pelanggan(db, pelanggan_id)
    if pelanggan is None:
        raise HTTPException(status_code=404, detail="Pelanggan not found")
    return pelanggan

#PEMESANAN
@router.get("/pemesanan/", response_model=PemesananListSchema)
async def get_all_pemesanan(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    pemesanan = crud.get_all_pemesanan(db, skip, limit)
    return {"data": pemesanan}

@router.get("/pemesanan/{pemesanan_id}", response_model=PemesananSchema)
async def get_pemesanan(db: Session = Depends(get_db), pemesanan_id: int = Path(..., title="Pemesanan ID")):
    pemesanan = crud.get_pemesanan(db, pemesanan_id)
    if pemesanan is None:
        raise HTTPException(status_code=404, detail="Pemesanan not found")
    return pemesanan

@router.post("/pemesanan/{pelanggan_id}", response_model=PemesananSchema)
async def create_pemesanan(pelanggan_id: int, pemesanan: PemesananSchema, db: Session = Depends(get_db)):
    return crud.create_pemesanan(db, pemesanan, pelanggan_id)

@router.put("/pemesanan/{id}", response_model=PemesananSchema)
async def update_pemesanan(id: int, updated_pemesanan: PemesananSchema, db: Session = Depends(get_db)):
    pemesanan = crud.update_pemesanan(db, id, updated_pemesanan)
    if pemesanan is None:
        raise HTTPException(status_code=404, detail="Pelanggan not found")
    return pemesanan

@router.delete("/pemesanan/{pemesanan_id}", response_model=PemesananSchema)
async def remove_pemesanan(pemesanan_id: int, db: Session = Depends(get_db)):
    pemesanan = crud.remove_pemesanan(db, pemesanan_id)
    if pemesanan is None:
        raise HTTPException(status_code=404, detail="Pemesanan not found")
    return pemesanan