from sqlalchemy.orm import Session
from models import Pelanggan, Pemesanan
from schemas import PelangganSchema, PemesananSchema

# Operasi CRUD untuk Pelanggan
def get_pelanggan(db: Session, pelanggan_id: int):
    return db.query(Pelanggan).filter(Pelanggan.id == pelanggan_id).first()

def create_pelanggan(db: Session, pelanggan: PelangganSchema):
    _pelanggan = Pelanggan(nama=pelanggan.nama, alamat=pelanggan.alamat, telepon=pelanggan.telepon)
    db.add(_pelanggan)
    db.commit()
    db.refresh(_pelanggan)
    return _pelanggan

def remove_pelanggan(db: Session, pelanggan_id: int):
    _pelanggan = get_pelanggan(db=db, pelanggan_id=pelanggan_id)
    db.delete(_pelanggan)
    db.commit()

def update_pelanggan(db: Session, pelanggan_id: int, nama: str, alamat: str, telepon: str):
    _pelanggan = get_pelanggan(db=db, pelanggan_id=pelanggan_id)
    _pelanggan.nama = nama
    _pelanggan.alamat = alamat
    _pelanggan.telepon = telepon
    db.commit()
    db.refresh(_pelanggan)
    return _pelanggan

# Operasi CRUD untuk Pemesanan
def get_pemesanan(db: Session, pemesanan_id: int):
    return db.query(Pemesanan).filter(Pemesanan.id == pemesanan_id).first()

def create_pemesanan(db: Session, pemesanan: PemesananSchema, pelanggan_id: int):
    _pemesanan = Pemesanan(deskripsi_sampah=pemesanan.deskripsi_sampah, pelanggan_id=pelanggan_id)
    db.add(_pemesanan)
    db.commit()
    db.refresh(_pemesanan)
    return _pemesanan

def remove_pemesanan(db: Session, pemesanan_id: int):
    _pemesanan = get_pemesanan(db=db, pemesanan_id=pemesanan_id)
    db.delete(_pemesanan)
    db.commit()

def update_pemesanan(db: Session, pemesanan_id: int, deskripsi_sampah: str):
    _pemesanan = get_pemesanan(db=db, pemesanan_id=pemesanan_id)
    _pemesanan.deskripsi_sampah = deskripsi_sampah
    db.commit()
    db.refresh(_pemesanan)
    return _pemesanan
