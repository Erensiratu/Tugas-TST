from pydantic import BaseModel
from typing import List, Optional

class PelangganSchema(BaseModel):
    id: Optional[int]
    nama: str
    alamat: str
    telepon: str

    class Config:
        orm_mode = True

class PemesananSchema(BaseModel):
    id: Optional[int]
    tanggal_pemesanan: str
    deskripsi_sampah: str
    status: str
    pelanggan_id: int

    class Config:
        orm_mode = True
