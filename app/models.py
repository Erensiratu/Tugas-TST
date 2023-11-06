from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config import Base
from datetime import datetime

class Pelanggan(Base):
    __tablename__ = "pelanggan"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    alamat = Column(String)
    telepon = Column(String)
    
    pemesanan = relationship("Pemesanan", back_populates="pelanggan")

class Pemesanan(Base):
    __tablename__ = "pemesanan"

    id = Column(Integer, primary_key=True, index=True)
    tanggal_pemesanan = Column(DateTime, default=datetime.utcnow)
    deskripsi_sampah = Column(String)
    status = Column(String, default="Pending")
    pelanggan_id = Column(Integer, ForeignKey("pelanggan.id"))
    
    pelanggan = relationship("Pelanggan", back_populates="pemesanan")
