from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.configdb import Base

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
    deskripsi_sampah = Column(String)
    status = Column(String, default="Pending")
    pelanggan_id = Column(Integer, ForeignKey("pelanggan.id"))
    
    pelanggan = relationship("Pelanggan", back_populates="pemesanan")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)