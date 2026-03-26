from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL
from database import Base
from datetime import datetime

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    email = Column(String(100), unique=True)
    password_hash = Column(String(255))


class Paquete(Base):
    __tablename__ = "paquetes"

    id = Column(Integer, primary_key=True)
    direccion = Column(String(255))
    estado = Column(String(50))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))


class Entrega(Base):
    __tablename__ = "entregas"

    id = Column(Integer, primary_key=True)
    paquete_id = Column(Integer, ForeignKey("paquetes.id"), unique=True)
    foto_url = Column(String(255))
    latitud = Column(DECIMAL(10,7))
    longitud = Column(DECIMAL(10,7))
    fecha_entrega = Column(DateTime, default=datetime.utcnow)