from pydantic import BaseModel
from datetime import datetime

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    nombre: str
    email: str
    password: str
    
class TokenResponse(BaseModel):
    access_token: str
    

class PaqueteResponse(BaseModel):
    id: int
    direccion: str
    estado: str

    class Config:
        orm_mode = True

class EntregaCreate(BaseModel):
    paquete_id: int
    foto_url: str
    lat: float
    lon: float

class EntregaResponse(BaseModel):
    id: int
    paquete_id: int
    foto_url: str
    latitud: float
    longitud: float
    fecha_entrega: datetime

    class Config:
        orm_mode = True