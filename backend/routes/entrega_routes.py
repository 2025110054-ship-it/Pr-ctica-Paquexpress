from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Paquete, Entrega
from schemas import PaqueteResponse, EntregaCreate
from typing import List
from auth import verify_token

router = APIRouter()

@router.get("/paquetes", response_model=List[PaqueteResponse])
def obtener_paquetes(
    db: Session = Depends(get_db), 
    user_data: dict = Depends(verify_token)
):
    user_id = user_data["user_id"]
    return db.query(Paquete).filter(Paquete.usuario_id == user_id).all()


@router.post("/entrega")
def registrar_entrega(
    data: EntregaCreate, 
    db: Session = Depends(get_db),
    user_data: dict = Depends(verify_token)
):
    user_id = user_data["user_id"]

    paquete = db.query(Paquete).filter(
        Paquete.id == data.paquete_id,
        Paquete.usuario_id == user_id
    ).first()

    if not paquete:
        raise HTTPException(
            status_code=404,
            detail="Paquete no encontrado o no autorizado"
        )

    if paquete.estado == "entregado":
        raise HTTPException(
            status_code=400,
            detail="Este paquete ya ha sido entregado previamente"
        )

    entrega_existente = db.query(Entrega).filter(
        Entrega.paquete_id == data.paquete_id
    ).first()

    if entrega_existente:
        raise HTTPException(
            status_code=400,
            detail="Ya existe un registro de entrega para este paquete"
        )

    nueva = Entrega(
        paquete_id=data.paquete_id,
        foto_url=data.foto_url,
        latitud=data.lat,
        longitud=data.lon
    )

    paquete.estado = "entregado"

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return {
        "mensaje": "Entrega registrada correctamente",
        "entrega_id": nueva.id
    }