from pydantic import BaseModel, EmailStr
from typing import List, Optional


class PelangganSchema(BaseModel):
    id: int
    nama: str 
    alamat: str
    telepon: str

class PemesananSchema(BaseModel):
    id: int
    deskripsi_sampah: str
    status: str
    pelanggan_id: int

class PelangganListSchema(BaseModel):
    data: List[PelangganSchema]

class PemesananListSchema(BaseModel):
    data: List[PemesananSchema]

#added

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config():
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None