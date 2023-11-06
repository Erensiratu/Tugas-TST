from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import PelangganSchema, PemesananSchema, Request, Response
import crud
from config import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/pelanggan/create")
async def create_pelanggan_service(request: Request[PelangganSchema], db: Session = Depends(get_db)):
    pelanggan = crud.create_pelanggan(db, pelanggan=request.parameter)
    return Response[PelangganSchema](status="Ok", code="200", message="Pelanggan created successfully", result=pelanggan)

@router.get("/pelanggan/{pelanggan_id}")
async def get_pelanggan_service(pelanggan_id: int, db: Session = Depends(get_db)):
    pelanggan = crud.get_pelanggan(db, pelanggan_id)
    if not pelanggan:
        raise HTTPException(status_code=404, detail="Pelanggan not found")
    return Response[PelangganSchema](status="Ok", code="200", message="Success fetch data", result=pelanggan)

@router.patch("/pelanggan/update/{pelanggan_id}")
async def update_pelanggan_service(pelanggan_id: int, request: Request[PelangganSchema], db: Session = Depends(get_db)):
    pelanggan = crud.update_pelanggan(db, pelanggan_id, nama=request.parameter.nama, alamat=request.parameter.alamat, telepon=request.parameter.telepon)
    if not pelanggan:
        raise HTTPException(status_code=404, detail="Pelanggan not found")
    return Response[PelangganSchema](status="Ok", code="200", message="Success update data", result=pelanggan)

@router.delete("/pelanggan/delete/{pelanggan_id}")
async def delete_pelanggan_service(pelanggan_id: int, db: Session = Depends(get_db)):
    pelanggan = crud.remove_pelanggan(db, pelanggan_id)
    if not pelanggan:
        raise HTTPException(status_code=404, detail="Pelanggan not found")
    return Response[PelangganSchema](status="Ok", code="200", message="Success delete data")

@router.post("/pemesanan/create")
async def create_pemesanan_service(request: Request[PemesananSchema], db: Session = Depends(get_db)):
    pemesanan = crud.create_pemesanan(db, pemesanan=request.parameter, pelanggan_id=request.parameter.pelanggan_id)
    return Response[PemesananSchema](status="Ok", code="200", message="Pemesanan created successfully", result=pemesanan)

@router.get("/pemesanan/{pemesanan_id}")
async def get_pemesanan_service(pemesanan_id: int, db: Session = Depends(get_db)):
    pemesanan = crud.get_pemesanan(db, pemesanan_id)
    if not pemesanan:
        raise HTTPException(status_code=404, detail="Pemesanan not found")
    return Response[PemesananSchema](status="Ok", code="200", message="Success fetch data", result=pemesanan)

@router.patch("/pemesanan/update/{pemesanan_id}")
async def update_pemesanan_service(pemesanan_id: int, request: Request[PemesananSchema], db: Session = Depends(get_db)):
    pemesanan = crud.update_pemesanan(db, pemesanan_id, deskripsi_sampah=request.parameter.deskripsi_sampah)
    if not pemesanan:
        raise HTTPException(status_code=404, detail="Pemesanan not found")
    return Response[PemesananSchema](status="Ok", code="200", message="Success update data", result=pemesanan)

@router.delete("/pemesanan/delete/{pemesanan_id}")
async def delete_pemesanan_service(pemesanan_id: int, db: Session = Depends(get_db)):
    pemesanan = crud.remove_pemesanan(db, pemesanan_id)
    if not pemesanan:
        raise HTTPException(status_code=404, detail="Pemesanan not found")
    return Response[PemesananSchema](status="Ok", code="200", message="Success delete data")
