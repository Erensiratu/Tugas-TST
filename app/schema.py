from pydantic import BaseModel
from typing import List


class PelangganSchema(BaseModel):
    id: int = None
    nama: str = None
    alamat: str = None
    telepon: str = None

class PemesananSchema(BaseModel):
    id: int = None
    deskripsi_sampah: str = None
    status: str = None
    pelanggan_id: int = None

class PelangganListSchema(BaseModel):
    data: List[PelangganSchema]

class PemesananListSchema(BaseModel):
    data: List[PemesananSchema]