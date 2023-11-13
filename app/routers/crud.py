from sqlalchemy.orm import Session
from ..models import Pelanggan, Pemesanan
from app.schema import PelangganSchema, PemesananSchema, PelangganListSchema, PemesananListSchema
from app.configdb import engine
from .. import oauth2
from fastapi import Depends

# Operasi CRUD untuk Pelanggan
def get_all_pelanggan(db: Session, skip: int = 0, limit: int = 100, current_user: int = Depends(oauth2.get_current_user)):
    return db.query(Pelanggan).offset(skip).limit(limit).all()

def get_pelanggan(db: Session, id: int):
    return db.query(Pelanggan).filter(Pelanggan.id == id).first()

def create_pelanggan(db: Session, pelanggan: PelangganSchema):
    _pelanggan = Pelanggan(id= pelanggan.id, nama=pelanggan.nama, alamat=pelanggan.alamat, telepon=pelanggan.telepon)
    db.add(_pelanggan)
    db.commit()
    db.refresh(_pelanggan)
    return _pelanggan

def remove_pelanggan(db: Session, id: int):
    _pelanggan = get_pelanggan(db=db, id=id)
    db.delete(_pelanggan)
    db.commit()

def update_pelanggan(db: Session, id: int, updated_pelanggan: PelangganSchema):
    _pelanggan = get_pelanggan(db=db, id=id)
    for field, value in updated_pelanggan.dict().items():
        setattr(_pelanggan, field, value)
    db.commit()
    db.refresh(_pelanggan)
    return _pelanggan

# Operasi CRUD untuk Pemesanan
def get_all_pemesanan(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pemesanan).offset(skip).limit(limit).all()

def get_pemesanan(db: Session, pemesanan_id: int):
    return db.query(Pemesanan).filter(Pemesanan.id == pemesanan_id).first()

def create_pemesanan(db: Session, pemesanan: PemesananSchema, pelanggan_id: int):
    _pemesanan = Pemesanan(id= pemesanan.id, deskripsi_sampah=pemesanan.deskripsi_sampah, status=pemesanan.status, pelanggan_id=pemesanan.pelanggan_id)
    db.add(_pemesanan)
    db.commit()
    db.refresh(_pemesanan)
    return _pemesanan

def remove_pemesanan(db: Session, pemesanan_id: int):
    _pemesanan = get_pemesanan(db=db, pemesanan_id=pemesanan_id)
    db.delete(_pemesanan)
    db.commit()

def update_pemesanan(db: Session, pemesanan_id: int, updated_pemesanan: PemesananSchema):
    _pemesanan= get_pemesanan(db=db, pemesanan_id=pemesanan_id)
    for field, value in updated_pemesanan.dict().items():
        setattr(_pemesanan, field, value)
    db.commit()
    db.refresh(_pemesanan)
    return _pemesanan
